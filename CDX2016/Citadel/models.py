from django.db import models
from django.contrib.auth.models import User
from re import sub

regex_expr_message = "[^A-Za-z0-9.,\-_?!'/+* ]"
regex_expr_usn = "[^A-Za-z0-9]"
regex_expr_names = "[^A-Za-z0-9 ]"

def removeCharactersMessage(string):
    return sub(regex_expr_message, "", string)

def removeCharactersUSN(string):
    return sub(regex_expr_usn, "", string)

def removeCharactersName(string):
    return sub(regex_expr_names, "", string)

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    name = models.CharField(max_length=64, unique=False)
    surname = models.CharField(max_length=128, unique=False)

    def save(self, *args, **kwargs):
        self.name = removeCharactersUSN(self.name)
        super(UserProfile, self).save(*args, **kwargs)

class BankingDetails(models.Model):
    name = models.CharField(max_length=64, unique=False)
    surname = models.CharField(max_length = 128, unique=False)
    Balance = models.DecimalField(max_digits=12, decimal_places=4)

    def save(self, *args, **kwargs):
        self.name = removeCharactersName(self.name)
        self.surname = removeCharactersName(self.surname)
        super(BankingDetails, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Banking details"

class NewsMessage(models.Model):
    poster = models.ForeignKey(User)
    title = models.CharField(max_length=45, unique=False)
    message = models.CharField(max_length=2048, unique=False)
    time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.message = removeCharactersMessage(self.message)
        self.title = removeCharactersMessage(self.title)
        super(NewsMessage, self).save(*args, **kwargs)