from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('colleges/',views.colleges,name='colleges'),
    path('colleges/<str:p>',views.collegesdetails,name='collegesdetails'),
    path('students/',views.students,name='students'),
    path('login/',views.login,name='login'),
    path('loginverification',views.loginverification,name='loginverification'),
    path('signup/',views.signup,name='signup'),
]