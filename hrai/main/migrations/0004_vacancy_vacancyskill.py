# Generated by Django 5.1.3 on 2024-11-21 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_resume_work_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('Программист', 'Программист'), ('Менеджер проекта', 'Менеджер проекта'), ('Инженер-программист', 'Инженер-программист'), ('Дизайнер UX/UI', 'Дизайнер UX/UI'), ('Data Scientist', 'Data Scientist'), ('Аналитик данных', 'Аналитик данных'), ('Тестировщик ПО', 'Тестировщик ПО'), ('DevOps-инженер', 'DevOps-инженер'), ('Frontend-разработчик', 'Frontend-разработчик'), ('Backend-разработчик', 'Backend-разработчик'), ('Fullstack-разработчик', 'Fullstack-разработчик'), ('Системный администратор', 'Системный администратор'), ('Специалист по кибербезопасности', 'Специалист по кибербезопасности'), ('Менеджер по продажам', 'Менеджер по продажам'), ('Маркетолог', 'Маркетолог'), ('Бухгалтер', 'Бухгалтер'), ('Юрист', 'Юрист'), ('HR-менеджер', 'HR-менеджер'), ('Руководитель проекта', 'Руководитель проекта'), ('Архитектор ПО', 'Архитектор ПО')], max_length=255, verbose_name='Должность')),
                ('salary', models.IntegerField(blank=True, null=True, verbose_name='Зарплата')),
                ('employment_type', models.CharField(choices=[('удаленная работа', 'Удаленная работа'), ('полная занятость', 'Полная занятость'), ('частичная занятость', 'Частичная занятость'), ('проектная работа', 'Проектная работа')], max_length=100, verbose_name='Тип занятости')),
                ('work_experience', models.IntegerField(blank=True, null=True, verbose_name='Опыт работы')),
            ],
        ),
        migrations.CreateModel(
            name='VacancySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.skill')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='main.vacancy')),
            ],
            options={
                'unique_together': {('vacancy', 'skill')},
            },
        ),
    ]
