from django.contrib import admin

# Register your models here.
from home.models import Project,Upload,Level,Currency,Replies,Proposals

class ProjectAdmin(admin.ModelAdmin):
    list_display=('title','author','description','price_type','price_min','price_max','level','admit_time','status','author','currency','upload_files' )

class LevelAdmin(admin.ModelAdmin):
    list_display=('level_type',)



admin.site.register(Project,ProjectAdmin)
admin.site.register(Level,LevelAdmin)
admin.site.register(Currency)
admin.site.register(Replies)
admin.site.register(Proposals)
