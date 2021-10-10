import random
import datetime

class Hacker_game():
    def __init__(self, company_income, company_security, hacker_resources, game_score):
        self.company_income = company_income
        self.company_security = company_security
        self.hacker_resources = hacker_resources
        self.game_score = game_score
        self.request = 0
        self.message = []
        '''
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
        '''
        #self.action()

    def set_action(self, action):
        self.request = int(action)

    def set_attrs(self, company_income, company_security, hacker_resources, game_score):
        self.company_income = company_income
        self.company_security = company_security
        self.hacker_resources = hacker_resources
        self.game_score = game_score

    def get_attrs(self):
        return self.company_income, self.company_security, self.hacker_resources, self.game_score

    def action_list(self, action):
        if action == 1:
            self.company_security += 2
        if action == 3:
            self.company_security += 1
            self.hacker_resources = self.hacker_resources - self.hacker_resources/4
            self.message.append('Мы обнаружили активность хакеров! Их ресурсы уменьшены на' + str(self.hacker_resources/4))

    def company(self):
        rost = random.randrange(0,5)
        if rost == 0:
            self.company_income += -10
            self.company_security += -2
            self.message.append('КРИЗИС!! Доходы компании упали на 10, ваш бюджет был урезан СЗИ = ' + str(self.company_security) + '!')

        if rost == 4:
            self.company_income += 10
            self.message.append('Ваша компания растет, ее бюджет увеличился на 10 единиц и составил ' + str(self.company_income) + '!')

    def hacker(self):
        attack = random.randrange(0,3)
        if attack == 0:
            self.hacker_resources += 3
        attack = attack * self.hacker_resources
        if attack == 2:
            self.message.append('Хакеры проводят мощную DoS-атаку!')
        return attack

    def action(self):
        self.message = []
        try:
            action = self.request
        except BaseException:
            action = 2
        self.action_list(action)

        if self.company_security > self.company_income/5:
            self.message = ['Вы тратите слишком много на эту дурацкую ИБ, ВЫ УВОЛЕНЫ!']
            return True, self.message

        attack = self.hacker()
        if attack > 0:
            if self.company_security < attack:
                self.message = ['Атака с силой ' + str(attack) + 'была успешна, мы потеряли все данные! ВЫ УВОЛЕНЫ!']
                return True, self.message
            else:
                self.message.append('Мы зафиксировали атаку, но успешно ее отбили!')

        else:
            self.message.append('Пока что все тихо уровень СЗИ = ' + str(self.company_security) + ' возможно хакеры затаились')

        self.game_score += 1
        self.company()
        self.message.append('СЗИ = ' + str(self.company_security) + ', бюджет компании =' + str(self.company_income) + '. Ваш выбор ? =')
        return False, self.message

'''print('Для начала игры введите свое имя')
name = input()
game = Hacker_game()
file = open('game_score.txt','a')
file.write(f'{datetime.datetime.now()}: {name} - {game.game_score}\n')
file.close()'''
