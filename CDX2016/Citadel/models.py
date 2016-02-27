from django.db import models
from django.contrib.auth.models import User
from re import sub

class StringSecurity:
    regex_expr_message = "[^A-Za-z0-9.,-_?! ]"
    regex_expr_usn = "[^A-Za-z0-9]"

    def removeCharactersMessage(self, string):
        return sub(self.regex_expr_message, "", string)

    def removeCharactersUSN(self, string):
        return sub(self.regex_expr_usn, "", string)


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    name = models.CharField(max_length=64, unique=False)
    surname = models.CharField(max_length=128, unique=False)

    def save(self, *args, **kwargs):
        self.name = StringSecurity.removeCharactersUSN(self.name)

class BankingDetails(models.Model):
    user = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        primary_key=True)
    Balance = models.DecimalField(max_digits=16, decimal_places=4)
    class Meta:
        verbose_name_plural = "Banking details"

class NewsMessage(models.Model):
    poster = models.ForeignKey(User)
    message = models.CharField(max_length=2048, unique=False)
    time = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        self.message = StringSecurity.removeCharactersMessage(self.message)
        super(NewsMessage, self).save(*args, **kwargs)