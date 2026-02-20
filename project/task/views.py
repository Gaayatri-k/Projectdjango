from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings

from .models import userdata
from .forms import signupForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
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
def login_page(request):
    return render(request,"login.html")
def loginverification(request):
    # return HttpResponse("Verifying Details.....")
    username=request.POST.get("username")
    password=request.POST.get("password")
    user=userdata.objects.filter(username=username,password=password).first()
    # if not user:
    #     print("Sorry,Enter a username to login.")
    #     return HttpResponse("Sorry,Enter a username to login.")
    if user:
        # user=authenticate(request,username=username,password=password)
        request.session['user_id']=user.id
        request.session['username']=user.username
        return redirect("welcome")
        # if user is not None:
        #     login(request,user)
        #     return redirect("welcome")
    else:
            print("Invalid Credentials enter correct username and password")
            return redirect("login")
def welcome(request):
    # if request.user.is_authenticated:
    #     return HttpResponse(f"<h1>Welcome {request.user.username}</h1>")
    username=request.session.get("username")
    if not username:
        return redirect("login")
    return HttpResponse(f"welcome {username}")


def signup(request):
    if request.method == 'POST':
        formdata = signupForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            return HttpResponse("Signup successful!")
    else:
        formdata = signupForm()

    return render(request, 'task/signupform.html', {'form': formdata})
def email(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        send_mail(
            subject,
            message,
            '',
            [""],
            fail_silently=False,
        )
        return HttpResponse("<h1>Email sent successfully</h1>")
    return render(request,"task/email.html")
        