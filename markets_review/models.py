from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey( User, on_delete=models.CASCADE, related_name="marekt_posts")
    image = CloudinaryField('image', default='placeholder')
    location = models.CharField(default = 'unknown')
    day_time = models.CharField(default='unknown')
    latitude = models.FloatField()
    longitude = models.FloatField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    review_rating = models.IntegerField()
