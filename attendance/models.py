from django.db import models
from django.contrib.auth.models import User
from employee.models import Profile
import requests
import datetime


def today_date():
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d")
    return today
def time_stamp():
    stamp_time = datetime.datetime.now()
    return stamp_time

# Create your models here.

class Holiday(models.Model):
    holiday = models.DateField(default = today_date)
    def __str__(self):
        return str(self.holiday)
    
class Bind(models.Model):
    ip = models.GenericIPAddressField(default = '')
    def __str__(self):
        return self.ip

class Attendance(models.Model):

    description = models.TextField(default = '')
    ip = models.GenericIPAddressField(default = '')
    date_today = models.DateField(default = today_date,verbose_name='Date') 
    created_at = models.DateTimeField(default= time_stamp)
    created_by = models.CharField(max_length=20,default = '')

    class Meta:
        unique_together = ('created_by', 'date_today',)
        
    def __str__(self):
        return self.created_by+' on '+str(self.date_today)





    
