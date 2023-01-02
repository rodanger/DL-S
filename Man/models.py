from email import message
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model): # Class Contact include all we need about the client information
    name = models.CharField(max_length=255, blank= True, null= True) 
    email = models.EmailField()
    address = models.CharField(max_length=255, blank= True, null= True)
    city = models.CharField(max_length=255, blank= True, null= True)
    state = models.CharField(max_length=255, blank= True, null= True)
    zip = models.CharField(max_length=255, blank= True, null= True)

    def __str__(self):
        return self.name