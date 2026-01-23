from django.http import HttpResponse
from django.shortcuts import render
from .forms import signupForm
# Create your views here.
students_data = {
    'students': [
        {'sno': 1, 'name': 'spandana', 'branch': 'CSE', 'age': 18},
        {'sno': 2, 'name': 'pallavi', 'branch': 'ECE', 'age': 20},
        {'sno': 3, 'name': 'bhavana', 'branch': 'IT', 'age': 18},
        {'sno': 4, 'name': 'raju', 'branch': 'AIML', 'age': 20},
        {'sno': 5, 'name': 'afeefa', 'branch': 'ECE', 'age': 20},
        {'sno': 6, 'name': 'gaayatri', 'branch': 'IT', 'age': 18},
    ]
}
items = {
    "svecw": {
        "name": "SHRI VISHNU ENGINEERING COLLEGE",
        "logo": "images/svecw.png"
    },
    "vit": {
        "name": "VISHNU INSTITUTE OF TECHNOLOGY",
        "logo": "images/vit.jpeg"
    },
    "bvrit": {
        "name": "BV RAJU INSTITUTE OF TECHNOLOGY",
        "logo": "images/bvrit.jpeg"
    }
}

def home(request):
    return render(request, 'task/home.html')

def colleges(request):
    return render(request, 'task/colleges.html',{
        "data":items,
    })
def collegesdetails(request, p):
    college = items.get(p)
    return render(request, 'task/collegesdetails.html', {
        "college": college
    })
def students(request):
    return render(request, 'task/students.html', students_data)
def login(request):
    return render(request,"login.html")
def loginverification(request):
    return HttpResponse("Verifying Details.....")
def signup(request):
    if request.method == 'POST':
        formdata = signupForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            return HttpResponse("Signup successful!")
    else:
        formdata = signupForm()

    return render(request, 'task/signupform.html', {'form': formdata})

        