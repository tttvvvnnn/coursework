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
    skills = []
    for key, value in skills_data.items():
        temp = []
        for x in value:
            temp.append((x, x))
        skills.extend(temp)

    full_name = forms.CharField(max_length=255, label='ФИО', widget=forms.TextInput(attrs={'placeholder': 'ФИО'}))
    position = forms.ChoiceField(choices=job_titles, label='Должность',
                                 widget=forms.Select(attrs={'id': 'jobTitle'}))  # choices заполняются в представлении
    skills = forms.MultipleChoiceField(choices=skills, label='Навыки', widget=forms.SelectMultiple(
        attrs={'id': 'skills'}))  # choices заполняются в представлении
    salary = forms.IntegerField(label='Зарплата', min_value=0,
                                widget=forms.NumberInput(
                                    attrs={'type': 'number', 'min': '0', 'step': '1', 'placeholder': 'Зарплата'}))
    work_experience = forms.IntegerField(label='Опыт работы', min_value=0, max_value=100,
                                         widget=forms.NumberInput(attrs={'type': 'number', 'min': '0', 'step': '1',
                                                                         'placeholder': 'Опыт работы(в годах)'}))

    employment_type = forms.ChoiceField(choices=[
        ('удаленная работа', 'Удаленная работа'),
        ('полная занятость', 'Полная занятость'),
        ('частичная занятость', 'Частичная занятость'),
        ('проектная работа', 'Проектная работа'),
    ], label='Тип занятости', widget=forms.Select())


class VacancyForm(forms.Form):
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
    skills = []
    for key, value in skills_data.items():
        temp = []
        for x in value:
            temp.append((x, x))
        skills.extend(temp)

    position = forms.ChoiceField(choices=job_titles, label='Должность',
                                 widget=forms.Select(attrs={'id': 'jobTitle'}))  # choices заполняются в представлении
    skills = forms.MultipleChoiceField(choices=skills, label='Навыки', widget=forms.SelectMultiple(
        attrs={'id': 'skills'}))  # choices заполняются в представлении
    salary = forms.IntegerField(label='Зарплата', min_value=0,
                                widget=forms.NumberInput(
                                    attrs={'type': 'number', 'min': '0', 'step': '1', 'placeholder': 'Зарплата'}))
    work_experience = forms.IntegerField(label='Опыт работы', min_value=0, max_value=100,
                                         widget=forms.NumberInput(attrs={'type': 'number', 'min': '0', 'step': '1',
                                                                         'placeholder': 'Опыт работы(в годах)'}))

    employment_type = forms.ChoiceField(choices=[
        ('удаленная работа', 'Удаленная работа'),
        ('полная занятость', 'Полная занятость'),
        ('частичная занятость', 'Частичная занятость'),
        ('проектная работа', 'Проектная работа'),
    ], label='Тип занятости', widget=forms.Select())
