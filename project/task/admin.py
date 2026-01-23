from django.contrib import admin
from .models import Department, studentdata
# Register your models here.
admin.site.register(studentdata)
admin.site.register(Department)