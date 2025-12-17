from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
colleges={
    'svecw':"shri vishnu",
     'vit':"vishnu",
}
def welcome(request):
    return HttpResponse("We")
def about(request):
    return HttpResponse("welcome to about page")
def department(request,college):
    clg=colleges[college]
    return HttpResponse(f"About page of {clg}")
def index(request):
    return HttpResponse("""i am index ,
                        i am index
                        i am index
                        i am index""")
def login(request):
    return redirect('index')