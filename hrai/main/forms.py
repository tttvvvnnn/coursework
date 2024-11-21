from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


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


JOB_TITLES = (
    ("Программист", "Программист"),
    ("Менеджер проекта", "Менеджер проекта"),
    ("Инженер-программист", "Инженер-программист"),
    ("Архитектор ПО", "Архитектор ПО"),
)

EMPLOYMENT_TYPES = (
    ("Удаленная работа", "Удаленная работа"),
    ("Полная занятость", "Полная занятость"),
    ("Частичная занятость", "Частичная занятость"),
    ("Проектная работа", "Проектная работа"),
)

EDUCATION_TYPES = (
    ("Бакалавриат", "Бакалавриат"),
    ("Специалитет", "Специалитет"),
    ("Магистратура", "Магистратура"),
    ("Среднее", "Среднее"),
)
skills_data = {
    "Программист": ["Python", "Java", "JavaScript", "C++", "C#", "PHP", "SQL", "NoSQL", "Git", "Docker",
                        "Kubernetes", "AWS", "Azure", "Google Cloud", "Agile", "Scrum", "Тестирование"],
}


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['fio', 'job_title', 'skills', 'desired_salary', 'employment_type', 'years_of_experience', 'education']
        widgets = {
            'job_title': forms.Select(choices=JOB_TITLES),
            'skills': forms.CheckboxSelectMultiple,
            'employment_type': forms.Select(choices=EMPLOYMENT_TYPES),
            'education': forms.Select(choices=EDUCATION_TYPES),
        }

    def __init__(self, *args, **kwargs):
        skills_data = kwargs.pop('skills_data', {})  # Получаем skills_data из kwargs
        super().__init__(*args, **kwargs)

        if self.data.get('job_title'):  # Если job_title есть в данных
            job_title = self.data.get('job_title')
            if job_title in skills_data:
                self.fields['skills'].choices = [(skill, skill) for skill in skills_data[job_title]]
