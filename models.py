from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=100)
    esal = models.FloatField()
    ecity = models.CharField(max_length=100) 

class Parent(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    message=models.CharField(max_length=100)
    studentname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    message=models.CharField(max_length=100)
    email=models.CharField(max_length=100)


