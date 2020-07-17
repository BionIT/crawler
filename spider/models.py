from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
    source = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, blank=True, default=0.00)
    userId = models.IntegerField()


