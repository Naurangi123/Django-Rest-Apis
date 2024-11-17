from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class StreamPlateform(models.Model):
    name=models.CharField(max_length=30)
    about=models.CharField(max_length=150)
    website=models.URLField(max_length=100)
    
    def __str__(self)->str:
        return f"Plateform - {self.name}"

def upload_to(instance, filename):
    return 'movieImages/{filename}'.format(filename=filename)

    
class WatchList(models.Model):
    title=models.CharField(max_length=50)
    # image = models.FileField(upload_to=upload_to,null=True,blank=True)
    storyline=models.CharField(max_length=200)
    plateform=models.ForeignKey(StreamPlateform, on_delete=models.CASCADE,related_name='watchlist')
    avg_rating=models.FloatField(default=0)
    number_rating=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f"movie - {self.title}  {self.plateform}"
    
    
class Review(models.Model):
    review_user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description=models.CharField(max_length=200,null=True)
    watchlist=models.ForeignKey(WatchList, on_delete=models.CASCADE,related_name="reviews")
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True) 
    
    def __str__(self) -> str:
        return f"{self.rating} | {self.watchlist.title} | {self.review_user}"