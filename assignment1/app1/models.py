from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER=[('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    DEPT=[('IT','IT'),
        ('CSE','CSE'),
        ('ECE','ECE'),
        ('EEE','EEE'),
        ('MECH','MECH'),
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
    dob = models.DateField()
    gender = models.CharField(max_length=10,choices=GENDER)
    dept = models.CharField(max_length=10,choices=DEPT)
    year = models.CharField(max_length=5,choices=YEAR)
    roll = models.CharField(max_length=20,unique=True)
    address = models.TextField()
    state = models.CharField(max_length=5,choices=STATE)
    pin = models.CharField(max_length=6)
    skills = models.CharField(max_length=100)
    mode = models.CharField(max_length=10,choices=MODE)

