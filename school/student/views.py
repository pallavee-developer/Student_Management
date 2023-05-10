from django.shortcuts import render,redirect

from student.form import AddStudentsForm


# Create your views here.
def index(request):
    return render(request,'index.html')

def courses(request):
    return render(request,'courses.html')


def signup(request):
    return render(request,'sign-up.html')

def dashboard(request):
    return render(request,'dashboard.html')

def viewstudents(request):
    return render(request,'viewstudents.html')

def profile(request):
    return render(request,'profile.html')


 