from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView,DetailView,CreateView,FormView, ListView
from home.forms import ProjectForm,RepliesForm
from django.contrib import messages
from home.models import Project, Replies
from django.db.models import Q
from django.views.generic import TemplateView,DetailView,CreateView,FormView,ListView
from home.forms import ProjectForm,RepliesForm,FilterForm
from django.contrib import messages
from .models import Project
# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'



class GetStartedView(TemplateView):
    template_name='get-started.html'


class ProjectProposalsView(ListView):
    template_name='project-proposals.html'
    paginate_by = 7

    def get_queryset(self):
        queryset = Replies.objects.filter(project=self.kwargs['id']).order_by('-created_at')    
        return queryset
    
   




class ProjectDetailView(CreateView):
    template_name='project-details.html'
    form_class=RepliesForm

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['detail'] = Project.objects.get(id=self.kwargs['id'])
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        if self.request.user:
            obj.user = self.request.user
            obj.project =  Project.objects.get(id=self.kwargs['id'])
        else:
            form.add_error('non_field_error', 'User should be loginned')
            return self.form_invalid(form)

        return super(ProjectDetailView, self).form_valid(form)
    
    def get_success_url(self, **kwargs):    
            url= f'/project-proposals/{self.kwargs["id"]}'     
            return url
        


class MyProfileView(TemplateView):
    template_name='my-profile.html'


class MyProfileEditView(TemplateView):
    template_name='my-profile-edit.html'

class SearchFreelancerView(ListView):
    template_name='search-freelancer.html'
    model=Project
    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     return Project.objects.filter(name__icontains=query)
    def get_queryset(self):
        query = self.request.GET.get('search')
        print(query)
        queryset=super().get_queryset()
        if query:
            
            queryset= queryset.filter(
                Q(title__icontains=query)                               
            )
        print(queryset)

        return  queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = FilterForm(initial={
            'search': self.request.GET.get('search', ''),
            
        })

        return context



class SearchJobView(TemplateView):
    template_name='search-job.html'
    context_object='results'
    
     
   
    
    
class MyProjectsEmployerView(ListView):
    template_name='my-projects-employer.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Project.objects.filter(author=self.request.user).order_by('-created_at')
        # self.paginate_by = self.request.GET.get('paginate_by', 10) or 10            
        return queryset

    def get(self, request):
        self.paginate_by = request.GET.get('paginate_by', 10) or 10
        print(self.paginate_by)
        data = Project.objects.filter(author=self.request.user).order_by('-created_at')
        print(data)
        paginator = Paginator(data, self.paginate_by)
        page = request.GET.get('page')

        try:
            self.paginated = paginator.get_page(page)
        except PageNotAnInteger:
            self.paginated = paginator.get_page(1)
        except EmptyPage:
            self.paginated = paginator.page(paginator.num_pages)
        
        print(self.paginated)

        return render(request, self.template_name, {'object_list':self.paginated, 'paginate_by':self.paginate_by,'page_obj':self.paginated})

class MyProjectsFreelancerView(ListView):
    template_name='my-projects-freelancer.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Project.objects.filter(author=self.request.user).order_by('-created_at')
        # self.paginate_by = self.request.GET.get('paginate_by', 10) or 10            
        return queryset

    def get(self, request):

        self.paginate_by = request.GET.get('paginate_by', 10) or 10
        print(self.paginate_by)
        data = Project.objects.filter(author=self.request.user).order_by('-created_at')
        print(data)
        paginator = Paginator(data, self.paginate_by)
        page = request.GET.get('page')

        try:
            self.paginated = paginator.get_page(page)
        except PageNotAnInteger:
            self.paginated = paginator.get_page(1)
        except EmptyPage:
            self.paginated = paginator.page(paginator.num_pages)
        
        print(self.paginated)

        return render(request, self.template_name, {'object_list':self.paginated, 'paginate_by':self.paginate_by,'page_obj':self.paginated})















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
    
        
