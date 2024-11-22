import json

from django.contrib import messages
from django.forms import formset_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import *
from .models import *


def main(request):
    return render(request, "main/main.html")


def create_resume(request):
    job_titles = [
        [
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
    ]  # Ваш список должностей

    skills_data = {
        "Программист": ["Python", "Java", "JavaScript", "C++", "C#", "PHP", "SQL", "NoSQL", "Git", "Docker",
                        "Kubernetes", "AWS", "Azure", "Google Cloud", "Agile", "Scrum", "Тестирование"],
        "Менеджер проекта": ["Agile", "Scrum", "Kanban", "Jira", "MS Project", "Управление рисками",
                             "Управление командой", "Планирование", "Бюджетирование", "Коммуникация"],
        "Инженер-программист": ["Python", "C++", "Java", "Embedded Systems", "Linux", "Hardware", "Firmware",
                                "Debugging", "Agile", "Scrum"],
        "Дизайнер UX/UI": ["Figma", "Sketch", "Adobe XD", "Photoshop", "Illustrator", "UI/UX дизайн", "User Research",
                           "Wireframing", "Prototyping", "Интерактивный дизайн"],
        "Data Scientist": ["Python", "R", "SQL", "Machine Learning", "Deep Learning", "Data Mining",
                           "Data Visualization", "Statistical Modeling", "Big Data"],
        "Аналитик данных": ["SQL", "Python", "R", "Tableau", "Power BI", "Data Mining", "Data Visualization",
                            "Statistical Analysis", "Анализ данных"],
        "Тестировщик ПО": ["Test Automation", "Selenium", "JUnit", "TestNG", "SQL", "Jira", "Agile", "Scrum",
                           "Black Box Testing", "White Box Testing"],
        "DevOps-инженер": ["Linux", "Docker", "Kubernetes", "AWS", "Azure", "Terraform", "Ansible", "CI/CD", "Git",
                           "Scripting"],
        "Frontend-разработчик": ["JavaScript", "HTML", "CSS", "React", "Angular", "Vue.js", "TypeScript", "Web Design",
                                 "Responsive Design"],
        "Backend-разработчик": ["Python", "Java", "Node.js", "PHP", "Ruby on Rails", "SQL", "NoSQL", "REST API",
                                "Microservices"],
        "Fullstack-разработчик": ["JavaScript", "HTML", "CSS", "Python", "Java", "Node.js", "React", "Angular", "SQL",
                                  "NoSQL", "REST API"],
        "Системный администратор": ["Linux", "Windows Server", "Networking", "Security", "Cloud Computing",
                                    "Virtualization", "Scripting", "Troubleshooting"],
        "Специалист по кибербезопасности": ["Security Auditing", "Penetration Testing", "Network Security",
                                            "Cloud Security", "Vulnerability Management", "Security Awareness"],
        "Менеджер по продажам": ["Sales Management", "Customer Relationship Management (CRM)", "Negotiation",
                                 "Lead Generation", "Sales Strategy", "Closing Deals"],
        "Маркетолог": ["Digital Marketing", "SEO", "SEM", "Social Media Marketing", "Content Marketing",
                       "Email Marketing", "Marketing Analytics"],
        "Бухгалтер": ["1С:Бухгалтерия", "MS Excel", "Налогообложение", "Бухгалтерский учет", "Финансовая отчетность",
                      "Auditing"],
        "Юрист": ["Гражданское право", "Уголовное право", "Хозяйственное право", "Договорное право",
                  "Корпоративное право"],
        "HR-менеджер": ["Recruitment", "Onboarding", "Performance Management", "Talent Acquisition", "HR Policies",
                        "Employee Relations"],
        "Руководитель проекта": ["Agile", "Scrum", "Kanban", "Project Management", "Risk Management", "Team Leadership",
                                 "Communication"],
        "Архитектор ПО": ["Software Design", "System Architecture", "Microservices", "Cloud Computing", "Databases",
                          "Security", "Agile"]
    }

    institutions = [
        "Среднее образование",
        "Московский государственный университет имени М.В. Ломоносова (МГУ)",
        "Санкт-Петербургский государственный университет (СПбГУ)",
        "Московский физико-технический институт (МФТИ)",
        "Высшая школа экономики (НИУ ВШЭ)",
        "Институт физики и технологий РАН",
        "Новосибирский государственный университет (НГУ)",
        "Казанский федеральный университет (КФУ)",
        "Уральский федеральный университет имени первого Президента России Б.Н. Ельцина (УрФУ)",
        "Томский государственный университет (ТГУ)",
        "Дальневосточный федеральный университет (ДВФУ)",
        "Сибирский федеральный университет (СФУ)",
        "Южный федеральный университет (ЮФУ)",
        "Российский государственный университет нефти и газа имени И.М. Губкина (РГУ нефти и газа)",
        "Российский химико-технологический университет имени Д.И. Менделеева (РХТУ)",
        "Московский авиационный институт (МАИ)",
        "Санкт-Петербургский политехнический университет Петра Великого (СПбПУ)",
        "Национальный исследовательский ядерный университет МИФИ (МИФИ)",
        "Российский университет дружбы народов (РУДН)",
        "Московский государственный технический университет имени Н.Э. Баумана (МГТУ им. Баумана)",
        "Санкт-Петербургский государственный электротехнический университет «ЛЭТИ» (ЛЭТИ)",
        "НИУ Белгородский государственный национальный исследовательский университет (НИУ БелГУ)",
        "Нижегородский государственный университет имени Н.И. Лобачевского (ННГУ)",
        "Тульский государственный университет (ТулГУ)",
        "Ивановский государственный химико-технологический университет (ИГХТУ)",
        "Самарский национальный исследовательский университет имени академика С.П. Королева (СамГУ)",
        "Воронежский государственный университет (ВГУ)",
        "Ростовский государственный университет (РГУ)",
        "Кубанский государственный университет (КубГУ)",
        "Алтайский государственный университет (АлтГУ)",
        "Иркутский государственный университет (ИГУ)",
        "Ярославский государственный университет имени П.Г. Демидова (ЯрГУ)",
        "Плехановский университет",
        "Российская академия народного хозяйства и государственной службы при Президенте Российской Федерации (РАНХиГС)",
    ]

    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            # Обработка данных формы (сохранение в базу данных)
            print(form.cleaned_data)
            resume = Resume(
                full_name=form.cleaned_data['full_name'],
                position=form.cleaned_data['position'],
                salary=form.cleaned_data['salary'],
                employment_type=form.cleaned_data['employment_type'],
                work_experience=form.cleaned_data['work_experience']
            )
            resume.save()

            for x in form.cleaned_data['skills']:
                skill = Skill(
                    name=x
                )
                skill.save()
                res_skill = ResumeSkill(
                    resume=resume,
                    skill=skill
                )
                res_skill.save()
            messages.success(request, 'Резюме успешно добавлено!')
            return render(request, 'main/create_resume.html', {'form': form})
        else:
            return JsonResponse({'no success': False, 'errors': form.errors})
    else:
        form = ResumeForm()
        form.fields['position'].choices = [(title, title) for title in job_titles]

        return render(request, 'main/create_resume.html', {
            'form': form,
            'job_titles': job_titles,  # Передаем данные в шаблон
            'skills_data': json.dumps(skills_data, ensure_ascii=False),
            # Преобразуем в JSON для использования в JavaScript
        })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Use the renamed function
            return redirect("{% url 'create_resume' %}")  # Redirect to your desired URL after signup
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form1': form})  # Correct template context


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('create_resume')
            else:
                return render(request, 'login', {'form2': form, 'error': 'Неверный логин или пароль'})
        else:
            return render(request, 'login', {'form2': form, 'errors': form.errors})
    else:
        form = LoginForm()
    return render(request, 'login', {'form2': form})


def list_resume(request):
    resumes = Resume.objects.all()
    print(resumes)
    return render(request, 'main/list_resume.html', {'resumes': resumes})


def create_vacancy(request):
    job_titles = [
        [
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
    ]  # Ваш список должностей

    skills_data = {
        "Программист": ["Python", "Java", "JavaScript", "C++", "C#", "PHP", "SQL", "NoSQL", "Git", "Docker",
                        "Kubernetes", "AWS", "Azure", "Google Cloud", "Agile", "Scrum", "Тестирование"],
        "Менеджер проекта": ["Agile", "Scrum", "Kanban", "Jira", "MS Project", "Управление рисками",
                             "Управление командой", "Планирование", "Бюджетирование", "Коммуникация"],
        "Инженер-программист": ["Python", "C++", "Java", "Embedded Systems", "Linux", "Hardware", "Firmware",
                                "Debugging", "Agile", "Scrum"],
        "Дизайнер UX/UI": ["Figma", "Sketch", "Adobe XD", "Photoshop", "Illustrator", "UI/UX дизайн",
                           "User Research",
                           "Wireframing", "Prototyping", "Интерактивный дизайн"],
        "Data Scientist": ["Python", "R", "SQL", "Machine Learning", "Deep Learning", "Data Mining",
                           "Data Visualization", "Statistical Modeling", "Big Data"],
        "Аналитик данных": ["SQL", "Python", "R", "Tableau", "Power BI", "Data Mining", "Data Visualization",
                            "Statistical Analysis", "Анализ данных"],
        "Тестировщик ПО": ["Test Automation", "Selenium", "JUnit", "TestNG", "SQL", "Jira", "Agile", "Scrum",
                           "Black Box Testing", "White Box Testing"],
        "DevOps-инженер": ["Linux", "Docker", "Kubernetes", "AWS", "Azure", "Terraform", "Ansible", "CI/CD", "Git",
                           "Scripting"],
        "Frontend-разработчик": ["JavaScript", "HTML", "CSS", "React", "Angular", "Vue.js", "TypeScript",
                                 "Web Design",
                                 "Responsive Design"],
        "Backend-разработчик": ["Python", "Java", "Node.js", "PHP", "Ruby on Rails", "SQL", "NoSQL", "REST API",
                                "Microservices"],
        "Fullstack-разработчик": ["JavaScript", "HTML", "CSS", "Python", "Java", "Node.js", "React", "Angular",
                                  "SQL",
                                  "NoSQL", "REST API"],
        "Системный администратор": ["Linux", "Windows Server", "Networking", "Security", "Cloud Computing",
                                    "Virtualization", "Scripting", "Troubleshooting"],
        "Специалист по кибербезопасности": ["Security Auditing", "Penetration Testing", "Network Security",
                                            "Cloud Security", "Vulnerability Management", "Security Awareness"],
        "Менеджер по продажам": ["Sales Management", "Customer Relationship Management (CRM)", "Negotiation",
                                 "Lead Generation", "Sales Strategy", "Closing Deals"],
        "Маркетолог": ["Digital Marketing", "SEO", "SEM", "Social Media Marketing", "Content Marketing",
                       "Email Marketing", "Marketing Analytics"],
        "Бухгалтер": ["1С:Бухгалтерия", "MS Excel", "Налогообложение", "Бухгалтерский учет",
                      "Финансовая отчетность",
                      "Auditing"],
        "Юрист": ["Гражданское право", "Уголовное право", "Хозяйственное право", "Договорное право",
                  "Корпоративное право"],
        "HR-менеджер": ["Recruitment", "Onboarding", "Performance Management", "Talent Acquisition", "HR Policies",
                        "Employee Relations"],
        "Руководитель проекта": ["Agile", "Scrum", "Kanban", "Project Management", "Risk Management",
                                 "Team Leadership",
                                 "Communication"],
        "Архитектор ПО": ["Software Design", "System Architecture", "Microservices", "Cloud Computing", "Databases",
                          "Security", "Agile"]
    }

    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            # Обработка данных формы (сохранение в базу данных)
            print(form.cleaned_data)
            vacancy = Vacancy(
                position=form.cleaned_data['position'],
                salary=form.cleaned_data['salary'],
                employment_type=form.cleaned_data['employment_type'],
                work_experience=form.cleaned_data['work_experience']
            )
            vacancy.save()

            for x in form.cleaned_data['skills']:
                skill = Skill(
                    name=x
                )
                skill.save()
                res_skill = VacancySkill(
                    vacancy=vacancy,
                    skill=skill
                )
                res_skill.save()
            messages.success(request, 'Резюме успешно добавлено!')
            return render(request, 'main/create_vacancy.html', {'form_vacancy': form})
        else:
            return JsonResponse({'no success': False, 'errors': form.errors})
    else:
        form = VacancyForm()
        form.fields['position'].choices = [(title, title) for title in job_titles]

        return render(request, 'main/create_vacancy.html', {
            'form_vacancy': form,
            'job_titles': job_titles,  # Передаем данные в шаблон
            'skills_data': json.dumps(skills_data, ensure_ascii=False),
            # Преобразуем в JSON для использования в JavaScript
        })


def list_vacancy(request):
    vacances = Vacancy.objects.all()
    return render(request, 'main/list_vacancy.html', {'vacances': vacances})


def calculate_match_score(vacancy, resume):
    """Вычисляет оценку соответствия резюме вакансии."""

    # a - должность
    a = 1.0 if vacancy.position == resume.position else 0.2

    # b - навыки
    vacancy_skills = set(vacancy.skills.values_list('skill__name',
                                                    flat=True))  # Используем двойной андерскор для доступа к полю name модели Skill
    resume_skills = set(resume.skills.values_list('skill__name',
                                                  flat=True))  # Используем двойной андерскор для доступа к полю name модели Skill
    common_skills = vacancy_skills.intersection(resume_skills)
    b = len(common_skills)

    # c - зарплата
    c = round((1.0 if resume.salary is None or vacancy.salary is None or vacancy.salary == resume.salary else min(
        vacancy.salary, resume.salary) / max(vacancy.salary,
                                             resume.salary) if vacancy.salary and resume.salary else 1.0), 2)

    # d - тип занятости
    d = round((1.0 if vacancy.employment_type == resume.employment_type else 0.2), 2)

    # e - опыт работы
    e = round((
        1.0 if resume.work_experience is None or vacancy.work_experience is None or vacancy.work_experience == resume.work_experience else resume.work_experience / vacancy.work_experience),
        2)
    score = a * b * c * d * e
    print(round(score, 2), a, b, c, d, e)
    return round(score, 2)


def current_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    resumes = Resume.objects.all()
    matched_resumes = []

    for resume in resumes:
        score = calculate_match_score(vacancy, resume)
        if (score != 0):
            matched_resumes.append((resume, score))

    # Сортируем резюме по оценке соответствия в порядке убывания
    matched_resumes.sort(key=lambda x: x[1], reverse=True)

    return render(request, 'main/current_vacancy.html', {
        'vacancy': vacancy,
        'matched_resumes': matched_resumes,
    })
