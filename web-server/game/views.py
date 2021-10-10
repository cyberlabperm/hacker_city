from django.shortcuts import render, redirect
from .models import Profile
from django.http import HttpResponse
from django.db import connection, connections
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import json
from hacker_game import Hacker_game

game = Hacker_game(100, 10, 5, 0)

def game_action(request):
    action = request.POST['action']
    username = request.COOKIES.get('username')
    user = Profile.objects.filter(username=username)[0]
    if game != None:
        game.set_action(action)
        end_game, message = game.action()
        company_income, company_security, hacker_resources, game_score = game.get_attrs()
        if end_game:
            message.append('Ваш результат = ' + str(user.game_score))
            message.append('Ваш лучший результат = ' + str(user.best_game_score))
            user.set_default()
            game.set_attrs(100, 10, 5, 0)
        else:
            user.set_attrs(company_income, company_security, hacker_resources, game_score)
        return HttpResponse(json.dumps(message))
    else:
        return HttpResponse('game is not found')

def home(request):
    cookie = request.COOKIES.get('username')
    if cookie != None:
        context = {'username': cookie}
        sql = 'SELECT * FROM game_profile WHERE \
                username=' + '"' + str(cookie) + '"'
        with connection.cursor() as cursor:
            cursor.execute(sql)
            usernames = cursor.fetchall()
            if len(usernames) != 0:
                for row in usernames:
                    company_income = row[3]
                    company_security = row[4]
                    hacker_resources = row[5]
                    game_score = row[6]
                    game.set_attrs(company_income, company_security, hacker_resources, game_score)
                    context['company_income'] = company_income
                    context['company_security'] = company_security
                return render(request, 'game/main_game.html', context)

    return render(request, 'game/auth.html')

def register(request):
    return render(request, 'game/register.html')

def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            error = 'Пароли не совпадают'
            return HttpResponse(json.dumps([-1, error]))

        if len(Profile.objects.filter(username=username)) != 0:
            error = 'Пользователь уже зарегистрирован'
            return HttpResponse(json.dumps([-1, error]))

        Profile.objects.create(
            username = username,
            password = password,
            company_income = 100,
            company_security = 10,
            hacker_resources = 5,
            game_score = 0,
            best_game_score = 0
        )
        message = 'Регистрация прошла успешно'
        return HttpResponse(json.dumps([1, message]))

def authentication(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #x" OR 1=1 ) --
        sql = 'SELECT * FROM game_profile WHERE \
                (username=' + '"' + username + '") \
                AND (password=' + '"' + password + '")'

        with connection.cursor() as cursor:
            cursor.execute(sql)
            if len(cursor.fetchall()) != 0:
                cursor.execute(sql)
                for row in cursor.fetchall():
                    company_income = row[3]
                    company_security = row[4]
                    hacker_resources = row[5]
                    game_score = row[6]
                game.set_attrs(company_income, company_security, hacker_resources, game_score)
                response = HttpResponse()
                response.set_cookie('username', str(username))
                return response
            else:
                error = 'Не верное имя пользователя или пароль'
                return HttpResponse(error)

def logout_view(request):
    if request.method == 'POST':
        response = HttpResponse('')
        response.delete_cookie('username')
        return response
