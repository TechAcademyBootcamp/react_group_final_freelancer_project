from django.shortcuts import render
from django.views.generic import TemplateView,DetailView

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

class SearchView(DetailView):
    teplate_name='search.html'
    model=''
    

class DashboardView(TemplateView):
    template_name='dashboard.html'
