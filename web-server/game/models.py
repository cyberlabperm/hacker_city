from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    company_income = models.IntegerField()
    company_security = models.IntegerField()
    hacker_resources = models.IntegerField()
    game_score = models.IntegerField()
    best_game_score = models.IntegerField()

    def set_attrs(self, company_income, company_security, hacker_resources, game_score):
        self.company_income = company_income
        self.company_security = company_security
        self.hacker_resources = hacker_resources
        self.game_score = game_score

        if game_score > self.best_game_score:
            self.best_game_score = game_score

        self.save()

    def set_default(self):
        self.company_income = 100
        self.company_security = 10
        self.hacker_resources = 5
        self.game_score = 0
        self.save()
