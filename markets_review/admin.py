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

# Register your models here.
admin.site.register(Review)
admin.site.register(Ratings)