from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from .models import Student
# class based and function based 
# Create your views here.
# def home(request):
#     # return HttpResponse("Hello")
#     return HttpResponse("<h2>hellooooooo</h2>")

# def register(request):
    
#     return render(request,'register.html')

    # class view 

class homeView(View):
    def get(self,request):
        users = Student.objects.all()
        return render(request,'home.html',{"users":users})
    
class StudentRegister(View):
    def get(self,request):
        return render(request,'register.html')
    
    def post(self,request):
        print(request.POST) #{as dictionary}
        name=request.POST.get("name")
        place=request.POST.get("place")
        age=request.POST.get("age")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        print(name,age,place,email,phone)
        Student.objects.create(name=name,place=place,age=age,email=email,phone=phone)
        return redirect("homeview")
    
class deletestudent(View):
    def get(self,request,**kwargs):
        stud_id=kwargs.get("id")
        student=Student.objects.get(id=stud_id)
        student.delete()
        return redirect("homeview")

class updatestudent(View):
    def get(self,request,**kwargs):
        stud_id = kwargs.get("id")
        student = Student.objects.get(id=stud_id)

        return render(request,"updateform.html",{"student":student})
    
    def post(self,request,**kwargs):
        student=Student.objects.get(id=kwargs.get("id"))
        name=request.POST.get("name")
        age=request.POST.get("age")
        place=request.POST.get("place")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        student.name=name
        student.place=place
        student.age=age
        student.email=email
        student.phone=phone
        student.save()
        return redirect("homeview")
        