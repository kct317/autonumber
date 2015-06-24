from django.contrib import admin
from .models import Article #models.py的Article
from .models import Person #models.py的Article
 
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title ','pub_date ','update_time ',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name ',)

admin.site.register(Article)
admin.site.register(Person)