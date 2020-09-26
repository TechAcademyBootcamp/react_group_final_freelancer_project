from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,CreateView,FormView
from home.forms import ProjectForm,RepliesForm
from django.contrib import messages
from home.models import Project

# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'



class GetStartedView(TemplateView):
    template_name='get-started.html'

class Project_DetailView(FormView):
    template_name='project-details.html'
    form_class=RepliesForm
    success_url='/'

    def form_valid(self,form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Project_DetailView, self).get_context_data(**kwargs)
        # context['detail'] = Project.objects.get(id=self.kwargs['id'])

        return context


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
    context_object_name='projects'
    success_url='/'

    def form_valid(self, form):
        messages.success(self.request, 'Mesajiniz Ugurla gonderildi!')
        project = form.save(commit=False)
        project.author = self.request.user
        project.save()
        return super().form_valid(form)
    
        
