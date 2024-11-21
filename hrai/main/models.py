from django.db import models

from django.db import models

class Resume(models.Model):
    fio = models.CharField(max_length=255, verbose_name="ФИО")
    job_title = models.CharField(max_length=255, verbose_name="Должность")
    skills = models.CharField(max_length=1000, blank=True, verbose_name="Навыки") # Храним как строку, разделенную запятыми
    desired_salary = models.IntegerField(verbose_name="Желаемая зарплата")
    employment_type = models.CharField(max_length=255, verbose_name="Тип занятости")
    years_of_experience = models.IntegerField(verbose_name="Опыт работы (в годах)")
    education = models.CharField(max_length=255, verbose_name="Образование")

    def __str__(self):
        return self.fio
