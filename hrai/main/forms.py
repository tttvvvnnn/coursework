from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обязательное поле. Введите действующий email.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}),
                               max_length=30, min_length=3)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               min_length=6)


class ResumeForm(forms.Form):
    full_name = forms.CharField(max_length=255, label='ФИО', widget=forms.TextInput(attrs={'placeholder': 'ФИО'}))
    position = forms.ChoiceField(choices=[], label='Должность',
                                 widget=forms.Select(attrs={'id': 'jobTitle'}))  # choices заполняются в представлении
    skills = forms.MultipleChoiceField(choices=[], label='Навыки', widget=forms.SelectMultiple(
        attrs={'id': 'skills'}))  # choices заполняются в представлении
    salary = forms.IntegerField(label='Зарплата', min_value=0,
                                widget=forms.NumberInput(
                                    attrs={'type': 'number', 'min': '0', 'step': '1', 'placeholder': 'Зарплата'}))

    employment_type = forms.ChoiceField(choices=[
        ('удаленная работа', 'Удаленная работа'),
        ('полная занятость', 'Полная занятость'),
        ('частичная занятость', 'Частичная занятость'),
        ('проектная работа', 'Проектная работа'),
    ], label='Тип занятости', widget=forms.Select())



