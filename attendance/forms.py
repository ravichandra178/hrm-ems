from django.forms import ModelForm
from django import forms
from .models import Attendance
import requests
from django.db import IntegrityError
import datetime


class AttendanceForm(ModelForm):
    #def f():
        #f = requests.request('GET', 'http://myip.dnsomatic.com')
        #ip = f.text
        #return ip
    class Meta:
        model = Attendance
        fields = ['description']
    #name = forms.CharField(label='Your Name')
    #status = forms.BooleanField(initial = True, label = 'status')
    #ip = forms.GenericIPAddressField(initial = f, label = 'ip', disabled = True)
    '''def clean_ip(self):
        data = self.cleaned_data['ip']
        if "175.101.99.142" not in data:
            raise forms.ValidationError("You have forgotten about Candies!")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data'''
    '''def clean(self):
        now = datetime.datetime.now()
        cleaned_data = self.cleaned_data
        date_today = cleaned_data['date_today']

        if date_today and Attendance.objects.get(date_today=date_today):
            raise forms.ValidationError("Already Submitted for Today")

        # Always return the full collection of cleaned data.
        return cleaned_data'''
    
    
        
