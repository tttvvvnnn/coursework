from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.main, name='home'),
    path('signup/', views.signup, name='signup'),
    # path('login/', views.login_view, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('create_resume/', views.create_resume, name='create_resume'),
    path('list_resume/', views.list_resume, name='list_resume'),
    path('create_vacancy/', views.create_vacancy, name='create_vacancy'),
    path('list_vacancy/', views.list_vacancy, name='list_vacancy'),
]
