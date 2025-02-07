from django.contrib import admin
from .models import Market, Review, Ratings
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Market)
class MarketAdmin(SummernoteModelAdmin):
    list_display = ('name', 'status', 'created_on')
    search_fields = ['name']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content',)


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('market', 'author', 'created_on', 'approved', )
    list_filter = ('approved', 'market',)


# Register your models here.
admin.site.register(Ratings)