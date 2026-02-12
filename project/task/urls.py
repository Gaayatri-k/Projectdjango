from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('colleges/',views.colleges,name='colleges'),
    path('colleges/<str:p>',views.collegesdetails,name='collegesdetails'),
    path('students/',views.students,name='students'),
    path('login/',views.login_page,name='login'),
    path('loginverification',views.loginverification,name='loginverification'),
    path('welcome/',views.welcome,name='welcome'),
    path('signup/',views.signup,name='signup'),
    path('email/',views.email,name='email'),
]