from django.contrib import admin
from .models import Attendance,Bind,GeneralHoliday

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    readonly_fields=('ip', )

@admin.register(GeneralHoliday)
class GeneralHolidayAdmin(admin.ModelAdmin):
    pass

@admin.register(Bind)
class BindAdmin(admin.ModelAdmin):
    pass




