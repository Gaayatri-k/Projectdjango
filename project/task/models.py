from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
class hello(models.Model):
    GENDER=[('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    YEAR=[('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
    ]
    STATE=[
        ('AP','AP'),
        ('TS','TS'),
        ('KA','KA'),
        ('TN','TN'),
    ]
    MODE=[('Online','Online'),
        ('Offline','Offline'),
        ('Hybrid','Hybrid'),
    ]
    name=models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10,choices=GENDER)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    year = models.CharField(max_length=5,choices=YEAR)
    roll = models.CharField(max_length=10,unique=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=5,choices=STATE)
    pin = models.CharField(max_length=6)
    skills = models.CharField(max_length=100)
    mode = models.CharField(max_length=10,choices=MODE)
class studentdata(models.Model):
    name=models.CharField(max_length=20)
class userdata(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=15)