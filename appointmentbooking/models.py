from django.db import models

# Create your models here.
from django.db.models import DateTimeField
from django.contrib.auth.models import User


class Doctor(models.Model):
    doctor_id= models.AutoField
    name = models.CharField(max_length=100, blank=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='pics', blank=True)
    department= models.CharField(max_length=100, blank=True)
    age=models.CharField(max_length=100, blank=True)
    email= models.CharField(max_length=100, blank=True)
    phone_number=models.CharField(max_length=100, blank=True)
    Specialist= models.CharField(max_length=100, blank=True)
    Experience=models.TextField(blank=True)
    level= models.CharField(max_length=100, blank=True)
    Passed_year =models.CharField(max_length=100, blank=True)
    E_description = models.TextField(blank=True)


    def __str__(self):
        return self.name







class Appointment(models.Model):
    Doctor_name = models.CharField(max_length=150)
    Department = models.CharField(max_length=100,null=True, blank=True)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Adress = models.CharField(max_length=100)
    Date_and_time = models.CharField(max_length=100)
    user_id = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.name


class Patient(models.Model):
    user = models.OneToOneField(User,null = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name



