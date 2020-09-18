from django.urls import path
from home.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post-project/', PostProjectView.as_view(), name='post-project'),
    path('get-started/', GetStartedView.as_view(), name='get-started'),
    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('my-profile-edit/', MyProfileEditView.as_view(), name='my-profile'),
    path('my-projects/', MyProjectsView.as_view(), name='my-projects'),

]
