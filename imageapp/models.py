from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    image = models.URLField()
