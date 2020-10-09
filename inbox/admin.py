from django.contrib import admin
from inbox.models import *

admin.site.register([Group, Message])
