from django.db import models

class student(models.Model):
    branch_choices = [
        ('CSE','Computer Science'),
        ('IT','Information Technology'),
        ('ECE','Electronics & Communication'),
        ('AI','Artificial Intelligence'),
        ('DS','Data Science'),
    ]

    year_choices = [
        (1,'1st year'),
        (2,'2nd year'),
        (3,'3rd year'),
        (4,'4th year'),
    ]

    gender_choices = [
        ('M','Male'),
        ('F','Female'),
        ('O','Others'),
    ]

    section_choices = [
        ('A','Section A'),
        ('B','Section B'),
        ('C','Section C'),
    ]

    stu_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    ph_no = models.CharField(max_length=15)
    branch = models.CharField(max_length=3, choices=branch_choices)
    year = models.IntegerField(choices=year_choices)
    section = models.CharField(max_length=1, choices=section_choices)
    gender = models.CharField(max_length=1, choices=gender_choices)
    dob = models.DateField()
    date_joined = models.DateField()
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    att_percent = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    scholarship_stat = models.BooleanField(default=False)
    address = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.name} ({self.stu_id})"
