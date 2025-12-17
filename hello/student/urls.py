from django.contrib import admin
from django.urls import path
from student import views
urlpatterns = [
    path('welcome/', views.welcome),
    path('about/', views.about),
    path('branch/<str:branchname>/', views.branch,name='branch'),
]