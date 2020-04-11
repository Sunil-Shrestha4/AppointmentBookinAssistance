from django.db import models

# Create your models here.
from django.db.models import DateTimeField


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
    Service1=models.TextField(blank=True)
    Service2=models.TextField(blank=True)
    Service3=models.TextField(blank=True)
    E1_workeds_as= models.CharField(max_length=100, blank=True)
    E1_start_to_end_date: models.CharField(max_length=100, blank=True)
    E1_description = models.TextField(blank=True)
    E2_workeds_as =models.CharField(max_length=100, blank=True)
    E2_start_to_end_date =models.CharField(max_length=100, blank=True)
    E2_description = models.TextField(blank=True)
    E3_workeds_as =models.CharField(max_length=100, blank=True)
    E3_start_to_end_date=models.CharField(max_length=100, blank=True)
    E3_description = models.TextField(blank=True)
    level= models.CharField(max_length=100, blank=True)
    Passed_year =models.CharField(max_length=100, blank=True)
    E_description = models.TextField(blank=True)

    def __str__(self):
        return self.name







class DrKiran(models.Model):
    items_json = models.CharField(max_length=100)
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Phone_number=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Adress =models.CharField(max_length=100)
    Date_and_time=models.DateTimeField()
