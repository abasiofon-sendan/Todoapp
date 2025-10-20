from django.db import models

class FruitStorage(models.Model):
    name= models.CharField(max_length=200)
    price=models.DecimalField(max_digits=5,decimal_places=2)
