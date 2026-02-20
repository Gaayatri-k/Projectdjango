from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import StudentForm

def reg(request):
    if request.method == 'POST':
        f = StudentForm(request.POST)
        if f.is_valid():
            s = f.save(commit=False)
            s.skills = ",".join(f.cleaned_data['skills'])
            s.save()
            return render(request,'success.html',{'s':s})
    else:
        f = StudentForm()
    return render(request,'app1/register.html',{'f':f})

