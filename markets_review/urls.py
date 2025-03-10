"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.market_list, name='home'),
    path('search/', views.search_view, name='search_results'),
    path('<slug:slug>/', views.market_detail, name='market_detail'),
    path('<slug:slug>/edit_review/<int:review_id>', views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>', views.review_delete, name='review_delete'),
]