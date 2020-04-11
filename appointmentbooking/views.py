from django.shortcuts import render
# Create your views here.
from math import ceil

from .models import Doctor, DrKiran
from django.core.mail import send_mail
from django .conf import settings


def index(request):


    return render(request,"index.html")

def doctors(request):
    # docts = Doctor.objects.all()
    # return render(request, "doctors.html", {'docts': docts})
    allDocts = []
    departdocts = Doctor.objects.values('department', 'id')
    departs= {item['department'] for item in departdocts}
    for depart in departs:
        doct = Doctor.objects.filter(department=depart)
        n = len(doct)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allDocts.append([doct, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allDocts': allDocts}
    return render(request,"doctors.html", params)


def register(request):
    return render(request,"register.html")

def departments(request):
    return render(request,"departments.html")

def about(request):
    return render(request,"about.html")

def elements(request):
    return render(request,"elements.html")

def blog_details(request):
    return render(request,"blog-details.html")

def blog_home(request):
    return render(request,"blog-home.html")

def contact(request):
    return render(request,"contact.html")

def view_profile(request,myid):
    doctor= Doctor.objects.filter(id=myid)
    return render(request, "abc.html", {'doctor': doctor[0]})

    # docts = Doctor.objects.all()
    # return render(request,"profile.html", {'docts': docts})

def datetime_picker(request):
    return render(request, "datetime-picker.html")

    # doctor = Doctor.objects.filter(id=myid)
    # return render(request, "datetime-picker.html", {'doctor': doctor[0]})
    #doctor = Doctor.objects.filter(id=myid)
    #return render(request, "datetime-picker.html",{'doctor': doctor[0]})




# def book(request):
#     if request.method=="POST":
#         First_name = request.POST['fname']
#         Last_name = request.POST['lname']
#         Email = request.POST['email']
#         Phone_number= request.POST['phone']
#         Adress = request.POST['adress']
#         Date_and_time= request.POST['date_time']
#
#     book = DrKiran(First_name = First_name,Last_name=Last_name,Email=Email,Phone_number=Phone_number,Adress=Adress,Date_and_time=Date_and_time)
#     book.save()
#
#     e_subject = "Booking COnfirmed!"
#     e_msg = "Thankyou for booking ! your booking has been confirmed"
#     e_mail = settings.EMAIL_HOST_USER
#
#     send_mail(
#         e_subject,
#         e_msg,
#         e_mail,
#         [Email]
#
#     )
#
#     return render(request,"datetime-picker.html",{"message": "You have book your Appointment with Dr. Kiran Bhusal, we will sent you confirmation mail"})
#




