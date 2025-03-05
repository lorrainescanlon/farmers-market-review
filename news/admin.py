from django.contrib import admin
from .models import News
from django_summernote.admin import SummernoteModelAdmin


@admin.register(News)
class News(SummernoteModelAdmin):

    list_display = ('title', 'status', 'created_on', 'author', )
    search_fields = ['title', 'author',]
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}  
    summernote_fields = ('content',)