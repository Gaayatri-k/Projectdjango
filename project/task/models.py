from django.db import models

# Create your models here.
class hello(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    branch=models.CharField(max_length=5)
class studentdata(models.Model):
    name=models.CharField(max_length=20)