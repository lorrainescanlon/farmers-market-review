from django.urls import path
from . import views

urlpatterns = [
    path('', views.market_list, name='home'),
    path('search/', views.search_view, name='search_results'),
    path('<slug:slug>/', views.market_detail, name='market_detail'),
    path('<slug:slug>/edit_review/<int:review_id>', views.review_edit,
         name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>', views.review_delete,
         name='review_delete'),
]
