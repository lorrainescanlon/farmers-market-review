import cloudinary
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
RATING = ((0, "0 *"), (1, "1 *"), (2, "2 *"), (3, "3 *"), (4, "4 *"), (5, "5 *"))
VISIT = ((0, "Yes"), (1, "No"))

# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey( User, on_delete=models.CASCADE, related_name="marekt_posts")
    image = CloudinaryField('image', default='placeholder')
    location = models.CharField(default = 'unknown')
    day_time = models.CharField(default='unknown')
    latitude = models.CharField()
    longitude = models.CharField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    review_rating = models.IntegerField()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.name} | written by {self.author}"

class Review(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField(max_length=400)
    stars_rating = models.IntegerField(choices=RATING, default= 5)
    visit_again = models.IntegerField(choices=VISIT, default = 0)
    approved = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"{self.market} {self.stars_rating} * review by {self.author} on {self.created_on}"

class Ratings(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name="market_ratings")
    stars = models.IntegerField()

    def __str__(self):
        return f"{self.market} - {self.stars}"