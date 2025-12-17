from django.contrib import admin
from django.urls import path
from students import views
urlpatterns = [
    path('welcome/', views.welcome),
    path('about/', views.about),
    path('index/', views.index),
    path('login/', views.login),
    path('department/<college>', views.department,name='department'),
]
