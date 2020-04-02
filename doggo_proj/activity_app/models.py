from django.db import models
from regLog_app.models import User

class Animal(models.Model):
    name= models.Charfield(max_length= 50)
    breed= models.Charfield(max_length=50)
    age= models.IntegerField()
    owner= models.ManyToManyField(User, related_name="animals")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tracker(models.Model):
    date=models.DateTimeField()
    animal = models.ForeignKey(Animal, related_name="tracking", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name="owner_tracking", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    morning_walk= models.BooleanField()
    afternoon_walk= models.BooleanField()
    evening_walk= models.BooleanField()
    breakfast= models.BooleanField()
    lunch= models.BooleanField()
    dinner= models.BooleanField()



