# prediction/models.py
from django.db import models

class House(models.Model):
    area = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()

class PredictionResult(models.Model):
    house = models.OneToOneField(House, on_delete=models.CASCADE)
    predicted_price = models.FloatField()
