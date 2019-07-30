from django.shortcuts import render
from .forms import AttendanceForm
from .models import Attendance,Bind,GeneralHoliday
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from datetime import date
import datetime
from django.http import HttpResponse
import requests
from attendance.templatetags.test import work
from employee.models import Profile

today = datetime.datetime.now()
today_day = today.strftime("%A")
this_day = datetime.date.today()



class AttendanceView(LoginRequiredMixin,FormView):
    template_name = 'attendance/index.html'
    form_class = AttendanceForm
    success_url = 'thanks/'
    
    
    def form_valid(self, form):
        bind_list = Bind.objects.values_list('ip',flat = True)
        holiday_list = GeneralHoliday.objects.values_list('holiday',flat = True)
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[-1].strip()
        else:
            ip_address = self.request.META.get('REMOTE_ADDR')
        if ip_address in bind_list:
            if this_day not in holiday_list:
                if today_day != 'Sunday':
                    fs=form.save(commit=False)
                    fs.created_by=self.request.user.username
                    fs.ip=ip_address
                    fs.save()
                    return super().form_valid(form)
                else:
                    return HttpResponse('You forgot to meet someone, Kindly trya9ain.!')
            else:
                return HttpResponse('Are You Sure?!')
        else:
            subject = 'Approve Bind'
            message = ip_address+' not in bind list'
            sender = self.request.user.email

            recipients = ['dashboard.mad@gmail.com'] 
            

            send_mail(subject, message, sender, recipients)
            return HttpResponse('Something terrible happened.! Kindly trya9ain.!')

class AttendanceList(LoginRequiredMixin,ListView):
    context_object_name = 'attendance_list'
    template_name = 'attendance/thanks.html'

    def get_queryset(self):
        return Attendance.objects.filter(created_by=self.request.user).filter(date_today__year=today.year,date_today__month=today.month)


def sal(request):
    list_profile = Profile.objects.filter(user = request.user)
    attendance_list = Attendance.objects.filter(created_by=request.user).filter(date_today__year=today.year,date_today__month=today.month)
    working_days = work()
    net_days = len(attendance_list)/working_days
    for object in list_profile:
        object.ns = net_days * object.salary
        object.save()
    return render(request,'attendance/salary.html',{'list_profile':list_profile})
    


    
        

        
