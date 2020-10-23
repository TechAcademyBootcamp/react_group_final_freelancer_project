from django.urls import path
from django.contrib.auth.decorators import login_required
from home.views import *
                    
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
    path('post-project/', login_required(ProjectView.as_view()), name='post-project'),
    path('project-detail/<int:id>', login_required(ProjectDetailView.as_view()), name='project-detail'),
    path('project-proposals/<int:id>', login_required(ProjectProposalsView.as_view()), name='project-proposals'),

    path('get-started/', GetStartedView.as_view(), name='get-started'),
    path('my-profile/', login_required(MyProfileView.as_view()), name='my-profile'),
    path('my-profile-edit/', login_required(MyProfileEditView.as_view()), name='my-profile-edit'),

    path('my-projects/employer', login_required(MyProjectsEmployerView.as_view()), name='my-projects-employer'),
    path('my-projects/freelancer', login_required(MyProjectsFreelancerView.as_view()), name='my-projects-freelancer'),

]
