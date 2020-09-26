from django.urls import path
from django.contrib.auth.decorators import login_required
from home.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post-project/', login_required(ProjectView.as_view()), name='post-project'),
    path('project-detail/<int:id>', login_required(Project_DetailView.as_view()), name='project-detail'),

    path('get-started/', GetStartedView.as_view(), name='get-started'),
    path('my-profile/', login_required(MyProfileView.as_view()), name='my-profile'),
    path('my-profile-edit/', login_required(MyProfileEditView.as_view()), name='my-profile'),
    path('my-projects/', login_required(MyProjectsView.as_view()), name='my-projects'),

]
