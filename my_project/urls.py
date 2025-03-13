from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('contact/', include("contact.urls"), name="contact-urls"),
    path('news/', include("news.urls"), name="news-urls"),
    path('summernote/', include('django_summernote.urls')),
    path('', include("markets_review.urls"), name='markets_review-urls'),
]

handler404 = 'my_project.views.handler404'
handler500 = 'my_project.views.handler500'
