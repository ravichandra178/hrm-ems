from django.urls import path
from .views import LeaveRequestCreate,success

app_name = 'leave'

urlpatterns = [
    path('', LeaveRequestCreate.as_view(), name = 'leaverequest_form'),
    path('success/', success ,name = 'success')
    ]
