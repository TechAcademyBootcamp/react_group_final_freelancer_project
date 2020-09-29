from django import template
from home.models import *

register = template.Library()

@register.filter(name='proposals')
def proposals(value): # Only one argument.
    x=Replies.objects.filter(project=value).count()
    return x

