
from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
def g():
    now = datetime.datetime.now()
    k = now.strftime("%Y-%m-%d")
    return k

def now():
        i=datetime.datetime.now()
        return i
today = now()
class LeaveRequest(models.Model):
    #name = models.OneToOneField(User,on_delete=models.CASCADE)
    reason = models.SlugField(max_length = 10,default = '')
    message = models.TextField()
    approve = models.BooleanField(default = False)
    from_date = models.DateField(default=g)
    to_date = models.DateField(default=g)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default= now)
    note = models.TextField(default = 'Pending')

    def __str__(self):
        return self.reason+'  '+self.note
    
    
