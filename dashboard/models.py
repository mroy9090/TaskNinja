from django.db import models

# Create your models here.


class Ipconfiguration(models.Model):
    interface_name=models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    description= models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    net_mask = models.CharField(max_length=100)
    
