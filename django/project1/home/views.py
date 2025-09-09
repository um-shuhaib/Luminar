from django.shortcuts import render
from django.http import HttpResponse

# class based and function based 
# Create your views here.
def home(request):
    # return HttpResponse("Hello")
    return HttpResponse("<h2>hellooooooo</h2>")

def register(request):
    student = ["Njanan","Neelima","Aromal"]
    return render(request,'register.html',{"user":student})