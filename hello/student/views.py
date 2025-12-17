from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse("<h1> welcome to home page")
def about(request):
    return HttpResponse("welcome to about page")
def branch(request,branchname):
    if branchname=='IT':
        return HttpResponse("IT branch details")
    elif branchname=='CSE':
        return HttpResponse("CSE branch details")
    else:
        return HttpResponse("no branch exists with the name")
    