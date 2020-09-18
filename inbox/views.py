from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.
class InboxView(TemplateView):
    template_name='inbox.html'


def room(request):
    return render(request, reverse_lazy('room'))