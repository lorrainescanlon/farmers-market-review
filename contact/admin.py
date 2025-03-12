from django.contrib import admin
from .models import Contact


# Register your models here.
@admin.register(Contact)
class Contact(admin.ModelAdmin):

    list_display = ('created_on', 'message', 'read', 'name', )
    search_fields = ['name']
    list_filter = ('read',)
