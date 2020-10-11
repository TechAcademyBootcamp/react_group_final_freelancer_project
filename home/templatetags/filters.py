from django import template
from home.models import *
from django.db.models import Q 
from datetime import datetime,timedelta,timezone
from pytz import timezone
import pytz

register = template.Library()

@register.filter(name='proposals')
def proposals(value): # Only one argument.
    x=Replies.objects.filter(project=value).count()
    return x

@register.filter(name='end_time')
def end_time(time): # Only one argument.
    print(time.replace(tzinfo=None))
    print(datetime.now().replace(tzinfo=None))

    x=time.replace(tzinfo=None)-datetime.now().replace(tzinfo=None)
    print(x)
    if x.total_seconds()<=0:
        return None
    days=x.days
    hours, rem=divmod(x.seconds,3600)
    if days<=1:
        days=str(days)+' day'
    else:
        days=str(days)+' days'
    
    if hours<=1:
        hours=str(hours)+' hour'
    else:
        hours=str(hours)+' hours'


    x=f'{days}, {hours}'




    return x


@register.filter(name='projects')
def projects(user): # Only one argument.
    x=Project.objects.filter(author=user).count()
    return x

@register.filter(name='sender')
def sender(group,id): # Only one argument.
    user=group.users.get(~Q(id = id))
    return f"{user.first_name} {user.last_name}"

@register.filter(name='group_messages')
def group_messages(group): # Only one argument.
    messages=group.messages.all()
    return messages

