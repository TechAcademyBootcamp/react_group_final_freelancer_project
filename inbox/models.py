from django.db import models
from django.utils.translation import ugettext as _

from home.models import Project
from accounts.models import CustomUser


User = CustomUser


class Group(models.Model):
    title = models.CharField(_('Title'), max_length=80, null=True, blank=True)
    project = models.ForeignKey(Project, verbose_name=_('Project'), on_delete=models.CASCADE, related_name='groups', null=True, blank=True)
    is_accepted = models.BooleanField('Is Accepted',default=False)
    users = models.ManyToManyField(User, related_name='messenger_groups')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    sender = models.ForeignKey(User, verbose_name=_('Sender'), on_delete=models.CASCADE, related_name='messages',)
    group = models.ForeignKey(Group, verbose_name=_('Group'), on_delete=models.CASCADE, related_name='messages',)
    text = models.TextField(_('Text'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    
