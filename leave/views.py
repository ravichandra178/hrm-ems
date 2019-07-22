from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import LeaveRequest
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

class LeaveRequestCreate(CreateView):
    model = LeaveRequest
    fields = ['reason','message','from_date','to_date']
    success_url = 'success/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        if form.is_valid():
            subject = form.cleaned_data['reason']
            message = form.cleaned_data['message']+' leave from '+str(form.cleaned_data['from_date'])+' to '+str(form.cleaned_data['to_date'])
            sender = self.request.user.email

            recipients = ['dashboard.mad@gmail.com'] 
            

            send_mail(subject, message, sender, recipients)
        return super().form_valid(form)

def success(request):
    leave_request = LeaveRequest.objects.all()
    return render(request,'leave/success.html',{'leave_request':leave_request})
