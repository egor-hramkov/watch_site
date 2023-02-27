from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Логин"}))
    email = forms.CharField(label="", widget=forms.EmailInput(attrs={'placeholder': "Email"}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': "Пароль"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': "Повторите пароль"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Логин"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': "Пароль"}))


class SearchProduct(forms.Form):
    searchBy = forms.CharField(max_length=150, label="", help_text="",
                               widget=forms.TextInput(attrs={'placeholder': 'Search'}))
