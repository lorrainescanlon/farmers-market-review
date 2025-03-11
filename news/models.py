from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# News Model.


class News(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_article"
    )
    content = models.TextField()
    excerpt = models.TextField(blank=False)
    image = CloudinaryField('image', null=True, default=None, blank=True)
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateField(auto_now=True)
    newsletter = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]
