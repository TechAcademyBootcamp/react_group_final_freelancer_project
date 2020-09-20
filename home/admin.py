from django.contrib import admin

# Register your models here.
from home.models import Project,Upload

class ProjectAdmin(admin.ModelAdmin):
    list_display=('title','author','short_description','long_description','price_type','price_min','price_max','level','admit_time','status','author','currency','upload_files' )



admin.site.register(Project,ProjectAdmin)