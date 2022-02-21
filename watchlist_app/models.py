from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# from tkinter import CASCADE

# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class WatchList(models.Model):
   title = models.CharField(max_length=50)
   platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist')
   stroyline = models.CharField(max_length=200) 
   active = models.BooleanField(default=True)
   created = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
       return self.title

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating)