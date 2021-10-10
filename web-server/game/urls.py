from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='game_home'),
    path('register', views.register, name='register'),
    url(r'^authentication/$', views.authentication, name='authentication'),
    url(r'^logout_view/$', views.logout_view, name='logout_view'),
    url(r'^create_user/$', views.create_user, name='create_user'),
    url(r'^game_action/$', views.game_action, name='game_action'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
