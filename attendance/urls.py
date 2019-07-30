from django.urls import path
from .views import AttendanceView,AttendanceList

app_name = 'attendance'

urlpatterns = [
    path('',AttendanceView.as_view(), name='attendance'),
    path('thanks/',AttendanceList.as_view() ,name = 'thanks'),
    path('salary/',sal ,name ='sal'),
    ]
