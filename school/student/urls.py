
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('courses/',views.courses, name='courses'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('signup/',views.signup, name='signup'),
    path('viewstudents/',views.viewstudents, name='viewstudents'),
    path('profile/',views.profile, name='profile'),
    
    
    
]