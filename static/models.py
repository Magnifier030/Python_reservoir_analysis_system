from django.db import models
# Create your models here.

class Water_data(models.Model):
    Reservoir_id = models.IntegerField()
    WaterLevel = models.IntegerField()
    EffectiveWaterStorageCapacity = models.FloatField()
    Reservoir_name = models.CharField(max_length=50, default="def")
    def ___str__(self):
        return self.title


class User_data(models.Model):
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    def __str__(self):
        return self.title