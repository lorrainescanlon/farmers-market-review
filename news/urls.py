from . import views
from django.urls import path

urlpatterns = [
    path('', views.NewsLetter.as_view(), name='news'),
]