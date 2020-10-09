from django import template
from home.models import *

register = template.Library()

@register.filter(name='proposals')
def proposals(value): # Only one argument.
    x=Replies.objects.filter(project=value).count()
    return x

@register.filter(name='projects')
def projects(user): # Only one argument.
    x=Project.objects.filter(author=user).count()
    return x

