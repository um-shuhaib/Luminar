from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=12)

    def __str__(self):
        return self.name