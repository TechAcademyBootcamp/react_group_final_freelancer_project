from django.shortcuts import render, redirect
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

    # def dispatch(self, request, *args, **kwargs):
        
    #     return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self,form):
        self.email=form.cleaned_data['email']
        return super().form_valid(form)
    
    def get_success_url(self):
        user=CustomUser.objects.get(email=self.email)
        sendConfirm(user)
        print("DISPACHHHHHDISPACHHHHHDISPACHHHHHDISPACHHHHHDISPACHHHHHDISPACHHHHHDISPACHHHHHDISPACHHHHHDISPACHHHHHDISPACHHHHH")
        if self.request.GET['next']:
            self.request.session['next'] = self.request.GET['next']
        print(self.request.session['next'])
        return super().get_success_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET['next']

        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPOSTTTTTTTTTTTTTT")

        print(self.request.POST)
        print(self.request.GET['next'])
        print(context)
        # print(self.re)
        if self.request.GET['next']:
            print("YESSSSSYESSSSSYESSSSSYESSSSSYESSSSSYESSSSSYESSSSSYESSSSSYESSSSSYESSSSSYESSSSS")
            context['next']=self.request.GET['next']
            print(context)
        
        return context

    
class LoginView(LoginView):
    template_name='login.html'
    authentication_form=LoginForm
    success_url=reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            next=self.request.GET['next']
        except:
            next=None
        if next:
            self.request.session['next']=next
        # context['next'] = self.request.GET['next']
        # print(self.request.GET['next'])
        print(context)
        return context

    def get_success_url(self):
      
        print("loginnnneddddddddddddddddddddddddddddddddd")
        print(self.request.session.get('next'))
        if self.request.session.get('next'):
            print("YEAG")
            next=self.request.session['next']
            self.request.session['next']=''
            return f"{next}"
        return super().get_success_url()