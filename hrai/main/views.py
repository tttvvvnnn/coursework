from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm


def main(request):
    return render(request, 'main/html/main.html')


def auth_home(request):
    job_titles = [
        "Программист",
        "Менеджер проекта",
        "Инженер-программист",
        "Дизайнер UX/UI",
        "Data Scientist",
        "Аналитик данных",
        "Тестировщик ПО",
        "DevOps-инженер",
        "Frontend-разработчик",
        "Backend-разработчик",
        "Fullstack-разработчик",
        "Системный администратор",
        "Специалист по кибербезопасности",
        "Менеджер по продажам",
        "Маркетолог",
        "Бухгалтер",
        "Юрист",
        "HR-менеджер",
        "Руководитель проекта",
        "Архитектор ПО"
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
    context = {'skills_data': skills_data, 'job_titles': job_titles}

    return render(request, 'main/html/auth_home.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Use the renamed function
            return redirect("{% url 'auth_home' %}")  # Redirect to your desired URL after signup
    else:
        form = SignUpForm()
    return render(request, 'main/html/signup.html', {'form1': form})  # Correct template context


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('auth_home')
            else:
                return render(request, 'main/html/login.html', {'form2': form, 'error': 'Неверный логин или пароль'})
        else:
            return render(request, 'main/html/login.html', {'form2': form, 'errors': form.errors})
    else:
        form = LoginForm()
    return render(request, 'main/html/login.html', {'form2': form})
