from django.db import models

from django.db import models


class Resume(models.Model):
    job_titles = [
            ["Программист", "Программист"],
            ["Менеджер проекта", "Менеджер проекта"],
            ["Инженер-программист", "Инженер-программист"],
            ["Дизайнер UX/UI", "Дизайнер UX/UI"],
            ["Data Scientist", "Data Scientist"],
            ["Аналитик данных", "Аналитик данных"],
            ["Тестировщик ПО", "Тестировщик ПО"],
            ["DevOps-инженер", "DevOps-инженер"],
            ["Frontend-разработчик", "Frontend-разработчик"],
            ["Backend-разработчик", "Backend-разработчик"],
            ["Fullstack-разработчик", "Fullstack-разработчик"],
            ["Системный администратор", "Системный администратор"],
            ["Специалист по кибербезопасности", "Специалист по кибербезопасности"],
            ["Менеджер по продажам", "Менеджер по продажам"],
            ["Маркетолог", "Маркетолог"],
            ["Бухгалтер", "Бухгалтер"],
            ["Юрист", "Юрист"],
            ["HR-менеджер", "HR-менеджер"],
            ["Руководитель проекта", "Руководитель проекта"],
            ["Архитектор ПО", "Архитектор ПО"]
        ]

    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=255, choices=job_titles, verbose_name='Должность')
    salary = models.IntegerField(verbose_name='Зарплата', null=True, blank=True)

    EMPLOYMENT_TYPE_CHOICES = [
        ('удаленная работа', 'Удаленная работа'),
        ('полная занятость', 'Полная занятость'),
        ('частичная занятость', 'Частичная занятость'),
        ('проектная работа', 'Проектная работа'),
    ]
    employment_type = models.CharField(max_length=100, choices=EMPLOYMENT_TYPE_CHOICES, verbose_name='Тип занятости')
    work_experience = models.IntegerField(verbose_name='Опыт работы', null=True, blank=True)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    name = models.CharField(max_length=255, verbose_name='Навык')

    def __str__(self):
        return self.name


class ResumeSkill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('resume', 'skill')  # Запрещает дубликаты навыков для одного резюме

    def __str__(self):
        return f"{self.resume} - {self.skill}"
