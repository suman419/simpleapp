from django.contrib import admin
from studentapp.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display=['sname','smobile','ssal','semail','saddress']

admin.site.register(Student,StudentAdmin)
