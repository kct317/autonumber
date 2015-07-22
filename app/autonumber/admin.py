from django.contrib import admin
from .models import *

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

class CaseAdmin(admin.ModelAdmin):
    list_display = ('casename', 'litigant', 'litiganttype', 'caseproperty', 'casevalue',
                    'fines', 'forfeituremoney', 'forfeitureitem', 'forfeitureamount', 'illegalfacts',
                    'law', 'punishbasis', 'createdate', 'informdate', 'informnumber',
                    'issueddate', 'decisionnumber', 'handlingunit', 'auditorman', 'remarkman',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(Case,CaseAdmin)