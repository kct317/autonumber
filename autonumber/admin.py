from django.contrib import admin
from .models import Article #models.py的Article
from .models import Person #models.py的Article
 
class ArticleAdmin(admin.ModelAdmin):  #未知这个有什么用
    list_display = ('title','pub_date','update_time',)
    search_fields = ('title', 'content',)
    list_filter = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'pub_date', 'update_time')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('title', 'content', 'pub_date', 'update_time')
        }),
    )

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Person,PersonAdmin)