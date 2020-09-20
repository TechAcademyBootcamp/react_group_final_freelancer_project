from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,CreateView
from home.forms import *
from django.contrib import messages

# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'


class PostProjectView(TemplateView):
    template_name='post-project.html'


class GetStartedView(TemplateView):
    template_name='get-started.html'


class MyProfileView(TemplateView):
    template_name='my-profile.html'


class MyProfileEditView(TemplateView):
    template_name='my-profile-edit.html'

class SearchView(TemplateView):
    template_name='search.html'
    
class MyProjectsView(TemplateView):
    template_name='my-projects.html'

class InboxView(TemplateView):
    template_name='inbox.html'



class DashboardView(TemplateView):
    template_name='dashboard.html'

class ProjectView(CreateView):
    form_class=ProjectForm
    template_name='post-project.html'
    success_url='/'

    def form_valid(self, *args, **kwargs):
        messages.success(self.request, 'Mesajiniz Ugurla gonderildi!')
        return super().form_valid(*args, **kwargs)
