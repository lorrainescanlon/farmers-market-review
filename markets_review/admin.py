from django.contrib import admin
from .models import Market, Review, Ratings

# Register your models here.
admin.site.register(Market)
admin.site.register(Review)
admin.site.register(Ratings)