from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView,DetailView,CreateView,FormView, ListView, UpdateView, View
from home.forms import ProjectForm,RepliesForm
from django.contrib import messages
from home.models import Project, Replies,Proposals
from django.db.models import Q
from django.views.generic import TemplateView,DetailView,CreateView,FormView,ListView
from home.forms import ProjectForm,RepliesForm,FilterForm
from datetime import datetime, timedelta

from django_email_verification import sendConfirm
from django.views.generic import TemplateView,DetailView,CreateView,FormView,ListView
from home.forms import *
from django.views.generic.edit import FormMixin
from django.contrib import messages
from .models import Project
from accounts.forms import *
from accounts.models import CustomUser
# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'



class GetStartedView(TemplateView):
    template_name='get-started.html'


class ProjectProposalsView(ListView,FormMixin):
    template_name = 'project-proposals.html'
    paginate_by = 7
    object_list=[]
    form_class = ProposalsForm
    success_url=reverse_lazy('inbox')

    def dispatch(self, request, *args, **kwargs):
        # do something extra here ...
        id=self.kwargs['id']
        print(id)
        print(Proposals.project_time(self,id))
        # if not Proposals.project_time(id):
        #     project=Project.objects.get(id=id)
        #     project.status=3
        #     project.save()

        return super(ProjectProposalsView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProjectProposalsView, self).get_context_data(**kwargs)
        context['detail'] = Project.objects.get(id=self.kwargs['id'])

        if context['detail'].status==2:
            context['reply1']=Replies.objects.get(project=context['detail'],user=context['detail'].proposals.get().user)
        return context

    def get_queryset(self):
        queryset = Replies.objects.filter(project=self.kwargs['id']).order_by('-created_at') 
        
        return queryset

    def validate(self,request):

        self.project=Project.objects.get(id=self.kwargs['id'])
        self.user1=self.request.user
        self.user2=CustomUser.objects.get(id=self.form.data['user_id'])
     
        if not self.project:
            self.form.add_error(None,'Project is not selected')
            return self.form_invalid(self.form)

        if not self.user1:
            self.form.add_error(None,'Login required')
            return self.form_invalid(self.form)

        if not self.user2:
            self.form.add_error(None,'User apllied on your project is required')
            return self.form_invalid(self.form)
 
        if not request.user.is_authenticated:
            self.form.add_error(None,'Login required')
            return self.form_invalid(self.form)
        
        if self.project.author != self.user1:
            self.form.add_error(None,'It is not your project')
            return self.form_invalid(self.form)
        
        if not self.project.replies.filter(user=self.user2).count():
            self.form.add_error(None,'This user have not applied on this project')
            return self.form_invalid(self.form)

        if not self.user2.active:
            self.form.add_error(None,"This user's profile is not activated")
            return self.form_invalid(self.form)

        self.group=Group.objects.filter(is_accepted=True,project=self.project,title=self.project.title,users=self.user1)

        if self.project.status !=1:
            self.form.add_error(None,"Project has already been closed")
            return self.form_invalid(self.form)

        self.group=Group.objects.filter(project=self.project,title=self.project.title ,users=self.user2).filter(users=self.user1)
        if 'chat' in self.request.POST:
            if self.group.count():
                self.form.add_error(None,"Chat with this user on this project has already been started")
                return self.form_invalid(self.form)
 

    def post(self, request, *args, **kwargs):
        self.queryset = Replies.objects.filter(project=self.kwargs['id']).order_by('-created_at')
        self.object_list=self.queryset
        self.form = self.get_form()

        self.validate(request)



        if self.form.is_valid():
            return self.form_valid(self.form)
        else:
            return self.form_invalid(self.form)



    def form_valid(self, form):
        if 'chat'in form.data:
            self.new_object=Group(project=self.project,title=self.project.title)
            self.new_object.save()
            self.new_object.users.add(self.user2)
            self.new_object.users.add(self.user1)
            self.new_object.save()
        elif 'accept' in form.data:

            if self.group.count():
                print('chat yaradilib ancaq indi accept olunur')
                self.new_object=self.group[0]
                self.new_object.is_accepted=True
                self.new_object.save()
                self.group=Group.objects.filter(project=self.project,title=self.project.title ,users=self.user2).filter(users=self.user1)
            else:
                print('chat yaradilmayib ve accept olunur')
                self.new_object=Group(is_accepted=True,project=self.project,title=self.project.title)
                self.new_object.save()
                self.new_object.users.add(self.user2)
                self.new_object.users.add(self.user1)
                self.new_object.save()
            
            obj=Proposals(user=self.user2,project=self.project)
            obj.save()
            
            self.project.status=2
            self.project.save()
        else: 
            self.form.add_error(None,"Method is not allowed")
            return self.form_invalid(self.form)
        

        
        return HttpResponseRedirect(self.get_success_url())
   




    # def get_queryset(self):
    #     queryset = Replies.objects.filter(project=self.kwargs['id']).order_by('-created_at')    
    #     return queryset
    
   




class ProjectDetailView(CreateView):
    template_name='project-details.html'
    form_class=RepliesForm

    def dispatch(self, request, *args, **kwargs):
        # do something extra here ...
        print('ASD')
        print(self.kwargs['id'])
        id=self.kwargs['id']
        project=Project.objects.get(id=id)
        print(project.admit_time)

        # id=self.kwargs['id']
        # if Proposals.project_time(id):
        #     project=Project.objects.get(id=id)
        #     project.status=3
        #     project.save()
        return super(ProjectDetailView, self).dispatch(request, *args, **kwargs)

    

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['detail'] = Project.objects.get(id=self.kwargs['id'])

        if context['detail'].status==2:
            context['reply']=Replies.objects.get(project=context['detail'],user=context['detail'].proposals.get().user)
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        print(self.request.user.active)
        if Project.objects.filter(id=self.kwargs['id']).count():
            if self.request.user:
                if self.request.user.active:
                    if self.request.user !=  Project.objects.get(id=self.kwargs['id']).author:
                        now = datetime.now()
                        time=now-timedelta(days=1)
                        count=Replies.objects.filter(user=self.request.user , created_at__gt=time).count()
                        if(count<3):
                            if not Replies.objects.filter(user=self.request.user, project=Project.objects.get(id=self.kwargs['id'])).count():
                                if Project.objects.get(id=self.kwargs['id']).status==1:
                                    obj.user = self.request.user
                                    obj.project =  Project.objects.get(id=self.kwargs['id'])
                                else:
                                    form.add_error(None, "This project has already been closed")
                                    return self.form_invalid(form)    
                            else:
                                form.add_error(None, "You can't apply on same project more than one")
                                return self.form_invalid(form)    
                        else:
                            form.add_error(None, "You can only apply 3 times in a day")
                            return self.form_invalid(form) 
                    else:
                        form.add_error(None, "You can't apply on your project")
                        return self.form_invalid(form)
                else:
                    form.add_error(None, "Your account is not activated. Checkout your profile")
                    return self.form_invalid(form)
            else:
                form.add_error(None, 'User should be loginned')
                return self.form_invalid(form)
        else:
            form.add_error(None, 'Project is not valid')
            return self.form_invalid(form)

        return super(ProjectDetailView, self).form_valid(form)
    
    def get_success_url(self, **kwargs):    
            url= f'/project-proposals/{self.kwargs["id"]}'     
            return url



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
        data = Project.objects.filter(author=self.request.user).order_by('-created_at')
        paginator = Paginator(data, self.paginate_by)
        page = request.GET.get('page')

        try:
            self.paginated = paginator.get_page(page)
        except PageNotAnInteger:
            self.paginated = paginator.get_page(1)
        except EmptyPage:
            self.paginated = paginator.page(paginator.num_pages)
        

        return render(request, self.template_name, {'object_list':self.paginated, 'paginate_by':self.paginate_by,'page_obj':self.paginated})

class MyProjectsFreelancerView(ListView):
    template_name='my-projects-freelancer.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Replies.objects.filter(author=self.request.user).order_by('-created_at')
        # self.paginate_by = self.request.GET.get('paginate_by', 10) or 10            
        return queryset

    def get(self, request):

        self.paginate_by = request.GET.get('paginate_by', 10) or 10
        data = Replies.objects.filter(user=self.request.user).order_by('-created_at')
        paginator = Paginator(data, self.paginate_by)
        page = request.GET.get('page')

        try:
            self.paginated = paginator.get_page(page)
        except PageNotAnInteger:
            self.paginated = paginator.get_page(1)
        except EmptyPage:
            self.paginated = paginator.page(paginator.num_pages)
        
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
    



# EDIT PROFILE


class MyProfileView(FormView):
    template_name='my-profile.html'
    form_class=ProfileForm
    success_url=reverse_lazy('my-profile')

    def get(self, request, *args, **kwargs): 
        if not request.user.active:
            messages.add_message(self.request, messages.INFO, 'Your account is not active')
        if not request.user.email_auth:
            messages.add_message(self.request, messages.INFO, 'Your email is not verified')
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        user=CustomUser.objects.get(id=self.request.user.id)

        first_name=form.cleaned_data['first_name']
        last_name=form.cleaned_data['last_name']
        overview=form.cleaned_data['overview']
        title=form.cleaned_data['title']
        hourly_price=form.cleaned_data['hourly_price']
        image=form.cleaned_data['image']
        skill=form.cleaned_data['skill']


        print(self.request.POST)
        
        
        
        if 'fullname' in self.request.POST:
            
            if not first_name:
                form.add_error('first_name', "This field can't be blank")
            if not last_name:
                form.add_error('last_name', "This field can't be blank")
                if not user.active:
                    messages.add_message(self.request, messages.INFO, 'Your account is not active')
                if not self.request.user.email_auth:
                    messages.add_message(self.request, messages.INFO, 'Your email is not verified')
                return self.form_invalid(form)
            elif first_name and last_name:
                user.first_name=first_name
                user.last_name=last_name
                messages.add_message(self.request, messages.INFO, 'Your fullname changed succesfully')
                user.save()
        elif 'Overview' in self.request.POST:
            if not overview:
                form.add_error('overview', "This field can't be blank")
                if not user.active:
                    messages.add_message(self.request, messages.INFO, 'Your account is not active')
                if not self.request.user.email_auth:
                    messages.add_message(self.request, messages.INFO, 'Your email is not verified')
                    
                return self.form_invalid(form)
            elif overview:
                user.overview=overview
                user.save()   
        elif 'Title' in self.request.POST:
            if not title:
                form.add_error('title', "This field can't be blank")
                if not user.active:
                    messages.add_message(self.request, messages.INFO, 'Your account is not active')
                if not self.request.user.email_auth:
                    messages.add_message(self.request, messages.INFO, 'Your email is not verified')
                return self.form_invalid(form)
            elif title:
                user.title=title
                user.save() 
        elif 'Hourly_price' in self.request.POST:
            if not hourly_price:
                form.add_error('hourly_price', "This field can't be blank")
                if not user.active:
                    messages.add_message(self.request, messages.INFO, 'Your account is not active')
                if not self.request.user.email_auth:
                    messages.add_message(self.request, messages.INFO, 'Your email is not verified')
                return self.form_invalid(form)
            elif hourly_price:
                user.hourly_price=hourly_price
                user.save()
        elif 'img' in self.request.POST:
            if not image:
                form.add_error('image', "This field can't be blank")
                if not user.active:
                    messages.add_message(self.request, messages.INFO, 'Your account is not active')
                if not self.request.user.email_auth:
                    messages.add_message(self.request, messages.INFO, 'Your email is not verified')
                return self.form_invalid(form)
            elif image:
                user.image=image
                user.save()  
        elif 'skills' in self.request.POST:
            print('skills')
            print(skill)
            print(skill.count())


            if not skill:
                form.add_error('skill', "This field can't be blank")
                if not user.active:
                    messages.add_message(self.request, messages.INFO, 'Your account is not active')
                if not self.request.user.email_auth:
                    messages.add_message(self.request, messages.INFO, 'Your email is not verified')
                return self.form_invalid(form)
            elif skill.count()>5:
                print('coxduu')
                form.add_error('skill', "Please enter at most 5 skills")
                if not user.active:
                    messages.add_message(self.request, messages.INFO, 'Your account is not active')
                if not self.request.user.email_auth:
                    messages.add_message(self.request, messages.INFO, 'Your email is not verified')
                return self.form_invalid(form)
            elif skill:
                user.skill.set(skill)
                user.save()  
        elif 'email-auth' in self.request.POST:
            sendConfirm(user)
            messages.add_message(self.request, messages.INFO, 'Verification email is sent')


        if user.first_name and user.last_name and user.title and user.overview and user.hourly_price and user.skill.count() and not user.active:
            user.active=True
            user.save()
            messages.add_message(self.request, messages.INFO, 'Your account is activated')   

        return super().form_valid(form)
    



class MyProfileEditView(TemplateView):
    template_name='my-profile-edit.html'