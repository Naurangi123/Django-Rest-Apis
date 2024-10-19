from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class StreamPlateform(models.Model):
    name=models.CharField(max_length=30)
    about=models.CharField(max_length=150)
    website=models.URLField(max_length=100)
    
    def __str__(self)->str:
        return f"Plateform - {self.name}"
    
    
class WatchList(models.Model):
    title=models.CharField(max_length=50)
    storyline=models.CharField(max_length=200)
    plateform=models.ForeignKey(StreamPlateform, on_delete=models.CASCADE,related_name='watchlist')
    created_at=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f"movie - {self.title}  {self.plateform}"
    
    
class Review(models.Model):
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description=models.CharField(max_length=200,null=True)
    watchlist=models.ForeignKey(WatchList, on_delete=models.CASCADE,related_name="reviews")
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True) 
    
    def __str__(self) -> str:
        return f"Rating - {self.rating}  movie - {self.watchlist.title}"