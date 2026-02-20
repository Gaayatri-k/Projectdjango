from django.db import models

# Create your models here.
class stu(models.Model):
    name=models.CharField(max_length=100)
    r_no=models.IntegerField(unique=True)
    email=models.EmailField()
    date_of_birth=models.DateField()
    is_active=models.BooleanField(default=True)
    age=models.IntegerField()