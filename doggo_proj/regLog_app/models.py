from __future__ import unicode_literals
from django.db import models
import re


class UserManager(models.Manager):
    def basic_validator(self,post_data):
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors= {}
        if len(post_data['email'])<1 or len(post_data['email'])>50:
            errors['email']= 'Email must be 1 to 50 characters'
        try: 
            User.objects.get(email=post_data['email'])
            errors['email']= 'Email already in use'
        except:
            pass
        if not email_regex.match(post_data['email']):
            errors['email'] = 'Email provided is invalid'

        if len(post_data['password'])< 8:
            errors['password'] = 'Password must be at least 8 characters'
        
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password']= 'Passwords do not match'
        
        return errors


class User(models.Model):
    first_name= models.CharField(max_length= 50)
    last_name= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    password= models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= UserManager()

