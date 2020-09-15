from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from accounts.models import *
from accounts.forms import *

# Create your views here.

class RegisterView(CreateView):
    template_name='register.html'
    form_class=RegisterForm
    success_url=reverse_lazy('login')
    
class LoginView(LoginView):
    template_name='login.html'
    authentication_form=LoginForm
    
    
    
