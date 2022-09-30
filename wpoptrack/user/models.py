from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, primary_key=True) 
    password = models.CharField(max_length=20)
    lat = models.FloatField()
    lon = models.FloatField()
