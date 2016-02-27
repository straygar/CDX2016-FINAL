from django import forms
from Citadel.models import UserProfile, BankingDetails, NewsMessage
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfForm(forms.ModelForm):
    name = forms.CharField()
    surname = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ("name", "surname",)