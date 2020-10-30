from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import RegisterForm, ProfileForm, LoginForm
from django.contrib.auth.models import User
from accounts.models import *
from django.utils.translation import gettext, gettext_lazy as _
# Register your models here.
from home.models import PriceType 
class SkillAdmin(admin.ModelAdmin):
    list_display=('title',)


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','email','username', 'password1', 'password2'),
        }),
    )

    # form = RegisterForm
    add_form = RegisterForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'active',)
    list_filter = ('is_staff', 'is_superuser', 'active','groups',)
    search_fields = ('username', 'first_name', 'last_name', 'email','id',)
    # ordering = ('username',)
    # filter_horizontal = ('groups', 'user_permissions',)


# admin.site.unregister(User)
admin.site.register(CustomUser,UserAdmin)
admin.site.register(Skill)
admin.site.register(PriceType)

