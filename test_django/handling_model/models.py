from django.db import models

class Location_of_camera(models.Model):
    camera_name=models.CharField(max_length=100)
    latitude=models.FloatField(max_length=1000)
    longitude=models.FloatField(max_length=1000)

class detected_database(models.Model):
    camera=models.ForeignKey(Location_of_camera,on_delete=models.CASCADE)
    Detected_date=models.DateTimeField(auto_now_add=True)
