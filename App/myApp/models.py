from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=10,null=True)
    quantity = models.IntegerField()
    categary=models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.productname
