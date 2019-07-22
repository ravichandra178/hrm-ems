from django import template
import calendar
import datetime
from attendance.models import GeneralHoliday


register = template.Library()

today = datetime.date.today()
this_month = today.strftime("%m")
holidays_list = GeneralHoliday.objects.values_list('holiday',flat = True)

@register.simple_tag
def work():
    now = datetime.datetime.now()
    cal = calendar.Calendar()
    working_days = len([x for x in cal.itermonthdays2(now.year, now.month) if x[0] !=0 and x[1] < 6])
    for i in holidays_list:
        if i.strftime("%m") == this_month:
            working_days = working_days - 1
    return working_days


	

