from django.db import models

# Create your models here.

class HotelSearch(models.Model):
    region_id=models.IntegerField()
    checkin=models.DateField()
    checkout=models.DateField()
    guests=models.JSONField()
    language=models.CharField(max_length=2)
    currency=models.CharField(max_length=3)
    residency=models.CharField(max_length=2)

    