from django.contrib import admin

# Register your models here.
from .models import School,Class,Student,Subject,Assessment_Areas,Answers,Awards,Summary

admin.site.register(School)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Assessment_Areas)
admin.site.register(Awards)
admin.site.register(Answers)
admin.site.register(Summary)