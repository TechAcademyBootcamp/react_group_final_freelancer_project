from django.urls import path
from inbox.views import *

urlpatterns = [
    path('', InboxView.as_view(), name='inbox'),
    path('room/', room, name='room')

]
