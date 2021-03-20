import random
import datetime

class hacker_game():
    def __init__(self):
        self.company_income = 100
        self.company_security = 10
        self.hacker_resources = 5
        self.game_score = 0
        print('Игра Blue vs Red\n',
              'Суть игры заключается в следующем:\n',
              '1) Вы руководите отделом информационной безопасности\n',
              '2) В любой момент времени вас могут начать атаковать хакеры\n',
              '3) Хакеры могут выжидать накапливая ресурсы для атаки\n',
              '4) У вас есть выбор - либо потратить ресурсы на СЗИ, либо сохранить ресурсы\n',
              '5) Атака считается успешной, если хакеры располагают большими ресурсами, чем было вложено в СЗИ\n',
              '6) Если вы тратите на ИБ больше 20% бюджета совет директоров впадает в ярость и вас увольняют!')
        print('Игра начинается!\n')
        print(f'Бюджет вашей компании равен {self.company_income} из них на ИБ тратится {self.company_security}')
        print('1) Потратить дополнительные ресурсы (2) на закупку СЗИ\n',
            '2) Ничего не делать\n',
            '3) Потратить (1) на проведение мониторинга и расследования активности хакеров (1)\n')
        self.action()
    def action_list(self,action):
        if action == 1:
            self.company_security += 2
        if action == 3:
            self.company_security += 1
            self.hacker_resources = self.hacker_resources - self.hacker_resources/4
            print(f'Мы обнаружили активность хакеров! Их ресурсы уменьшены на {self.hacker_resources/4}')
         
    def company(self):
        rost = random.randrange(0,5)
        if rost == 0:
            self.company_income += -10
            self.company_security += -2
            print(f'КРИЗИС!! Доходы компании упали на 10, ваш бюджет был урезан СЗИ = {self.company_security}!')
            
        if rost == 4:
            self.company_income += 10
            print(f'Ваша компания растет, ее бюджет увеличился на 10 единиц и составил {self.company_income}!')

    def hacker(self):
        attack = random.randrange(0,3)
        if attack == 0:
            self.hacker_resources += 3
        attack = attack * self.hacker_resources
        if attack == 2:
            print('Хакеры проводят мощную DoS-атаку!')
        return attack
    
    def action(self):
        while True:
            print(f'СЗИ = {self.company_security}, бюджет компании ={self.company_income}. Ваш выбор ? =')
            try:
                action = int(input())
            except BaseException:
                action = 2
            self.action_list(action)
            
            if self.company_security > self.company_income/5:
                print('Вы тратите слишком много на эту дурацкую ИБ, ВЫ УВОЛЕНЫ!')
                break
            
            attack = self.hacker()
            if attack > 0:
                if self.company_security  < attack:
                    print(f'Атака с силой {attack} была успешна, мы потеряли все данные! ВЫ УВОЛЕНЫ!')
                    break               
                else:
                    print('Мы зафиксировали атаку, но успешно ее отбили!')
            
            else:
                print(f'Пока что все тихо уровень СЗИ = {self.company_security}, возможно хакеры затаились')
            self.game_score += 1   
            self.company()
            
print('Для начала игры введите свое имя')
name = input()
game = hacker_game()
file = open('game_score.txt','a')
file.write(f'{datetime.datetime.now()}: {name} - {game.game_score}\n')
file.close()


    
    

