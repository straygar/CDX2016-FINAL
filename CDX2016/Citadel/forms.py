from django import forms
from Citadel.models import UserProfile, BankingDetails, NewsMessage
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(), required=True, label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Password")
    email = forms.EmailField(widget=forms.EmailInput(), required=True, label="Email")
    captcha = CaptchaField(required=True, label="Verify you are not a robot")
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, label="Name")
    surname = forms.CharField(widget=forms.TextInput(), required=True, label="Surname")

    class Meta:
        model = UserProfile
        fields = ("name", "surname",)

class UserLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), required=True, label="Username", max_length=User._meta.get_field("username").max_length)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Password")
    captcha = CaptchaField(required=True, label="Verify you are not a robot")
