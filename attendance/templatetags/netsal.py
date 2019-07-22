from .test import work
from employee.models import Profile
from django import template
import requests
from django.contrib.auth.models import User

register = template.Library()
d = work()
def game(request):
    user_name = request.user
    return user_name

@register.simple_tag
def net_salary():
    pass
    #profile_list = Profile.objects.values_list('salary',flat = True).filter(user__iexact=game)
    #new = ''
    #for i in profile_list:
        #new+=i
    
    #per_day = new/d
    #return per_day

