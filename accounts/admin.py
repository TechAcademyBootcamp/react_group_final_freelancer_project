from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import *
# Register your models here.


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Skill)