from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from watch_shop.models import Orders


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Логин"}))
    email = forms.CharField(label="", widget=forms.EmailInput(attrs={'placeholder': "Email"}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': "Пароль"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': "Повторите пароль"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже зарегистрирован")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Пользователь с таким логином уже зарегистрирован")
        return username

    def clean_password1(self):
        password = self.cleaned_data['password1']
        if len(password) < 8 or " " in password:
            raise ValidationError('Пароль должен быть больше 7 символов и не содержать пробелов')
        return password

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('Пароли не совпадают')
        return password2


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Логин"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': "Пароль"}))


class SearchProduct(forms.Form):
    searchBy = forms.CharField(max_length=150, label="", help_text="",
                               widget=forms.TextInput(attrs={'placeholder': 'Search'}))


class RegisterOrder(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['address', 'phone']


class FilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['manufacturer'].empty_label = "Производитель"
        self.fields['belt_type'].empty_label = "Материал ремешка"
        self.fields['gender'].empty_label = "Пол"
        self.fields['price_start'].placeholder = "От"
        self.fields['price_end'].placeholder = "До"

    price_start = forms.CharField(max_length=10)
    price_end = forms.CharField(max_length=10)
    manufacturer = forms.Select()
    belt_type = forms.Select()
    gender = forms.Select()
    is_water_resist = forms.CheckboxInput()
