from django.db import models

# Create your models here.
class Article(models.Model):
    SKU = models.CharField(max_length = 50)
    name =models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    
    def __str__(self):
        return self.SKU +" " + self.name