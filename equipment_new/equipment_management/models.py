from django.db import models
import openpyxl
from datetime import datetime

class Equipment(models.Model):

    device_name = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=150,  null=True, blank=True)
    quantity = models.IntegerField( null=True, blank=True )
    audit = models.DateField( null=True, blank=True )
    location = models.CharField(max_length=150,  null=True, blank=True )
    status = models.CharField(max_length=150,  null=True, blank=True )
    comments = models.CharField(max_length=2000,  null=True, blank=True )

    def __str__(self):
        return self.device_name
    
