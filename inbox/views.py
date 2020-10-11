from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.db.models import Q 
# Create your views here.
class InboxView(TemplateView):
    template_name='inbox15.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['groups'] = self.request.user.messenger_groups.all()
        # context['groups'] = self.request.user.messenger_groups.all()

        return context


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })