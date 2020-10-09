from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from accounts.models import *
from accounts.forms import *
from django_email_verification import sendConfirm

# Create your views here.

class RegisterView(CreateView):
    template_name='register.html'
    form_class=RegisterForm
    success_url=reverse_lazy('login')

    def form_valid(self,form):
        self.email=form.cleaned_data['email']
        return super().form_valid(form)
    
    def get_success_url(self):
        user=CustomUser.objects.get(email=self.email)
        sendConfirm(user)
        return super().get_success_url()
    
class LoginView(LoginView):
    template_name='login.html'
    authentication_form=LoginForm
    
    
    
