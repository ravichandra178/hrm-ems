from django.contrib import admin
from .models import Attendance,Bind,Holiday

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    readonly_fields=('ip', )

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    pass

@admin.register(Bind)
class BindAdmin(admin.ModelAdmin):
    pass




