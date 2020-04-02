from django.db import models

class Animal(models.Model):
    name= models.Charfield(max_length= 50)
    breed= models.Charfield(max_length=50)
    age= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tracker(models.Model):
    date=models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    morning_walk=models.BooleanField()
    afternoon_walk= models.BooleanField()
    evening_walk=models.BooleanField()
    walk_time=models.DurationField()
    breakfast=models.BooleanField()
    lunch=models.BooleanField()
    dinner=models.BooleanField()





