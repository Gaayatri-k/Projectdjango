from django.shortcuts import render

# Create your views here.
students_data = {
    'students': [
        {'sno': 1, 'name': 'spandana', 'branch': 'CSE', 'age': 18},
        {'sno': 2, 'name': 'pallavi', 'branch': 'ECE', 'age': 20},
        {'sno': 3, 'name': 'bhavana', 'branch': 'IT', 'age': 18},
        {'sno': 4, 'name': 'subbu', 'branch': 'AIML', 'age': 20},
        {'sno': 5, 'name': 'afeefa', 'branch': 'ECE', 'age': 20},
        {'sno': 6, 'name': 'gaayatri', 'branch': 'IT', 'age': 18},
    ]
}

def home(request):
    return render(request, 'task/home.html')

def colleges(request):
    return render(request, 'task/colleges.html')

def students(request):
    return render(request, 'task/students.html', students_data)