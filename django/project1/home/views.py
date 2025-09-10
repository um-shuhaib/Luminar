from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
# class based and function based 
# Create your views here.
def home(request):
    # return HttpResponse("Hello")
    return HttpResponse("<h2>hellooooooo</h2>")

def register(request):
    student = ["Njanan","Neelima","Aromal"]
    return render(request,'register.html',{"user":student})

    # class view 

class homeView(View):
    def get(self,request):
        users = User.objects.all()
        return render(request,'home.html',{"users":users})