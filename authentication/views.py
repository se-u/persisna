from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
# Create your views here.

class Login(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm

class Logout(LogoutView):
    pass
