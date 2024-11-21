from django.contrib import admin

from .models import ResumeSkill, Resume  # замените на вашу модель


admin.site.register(ResumeSkill)
admin.site.register(Resume)
