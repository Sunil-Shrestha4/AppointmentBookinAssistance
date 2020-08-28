from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from math import ceil
from django.contrib.auth.models import User, auth
from .models import Doctor, Appointment, Patient
from django.core.mail import send_mail
from django .conf import settings
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
def index(request):


    return render(request,"index.html")
# def logout(request):
#     auth.logout(request)
#     return redirect('/')

@login_required(login_url='login')
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




def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.name.lower() or query in item.name.upper() or query in item.department.lower():
        return True
    else:
        return False



def search(request):
    query = request.GET.get('search')
    allDocts = []
    departdocts = Doctor.objects.values('department', 'id')
    departs = {item['department'] for item in departdocts}
    for depart in departs:
        docttemp = Doctor.objects.filter(department=depart)
        doct = [item for item in docttemp if searchMatch(query, item)]

        n = len(doct)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(doct)!=0:
            allDocts.append([doct, range(1, nSlides), nSlides])
    params = {'allDocts': allDocts, "msg": ""}
    if len(allDocts) == 0 or len(query)<3:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'search.html', params)





def register(request):
    return render(request,"nav.html")

def departments(request):
    return render(request,"nav.html")

def about(request):
    return render(request,"about.html")

# def login(request):
#     return render(request,"login.html")

def blog_details(request):
    return render(request,"blog-details.html")

def blog_home(request):
    return render(request,"blog-home.html")

def contact(request):
    return render(request,"contact.html")

def logout(request):
    auth.logout(request)
    return render(request,"/")

@login_required(login_url='login')
def view_profile(request,myid):
    doctor= Doctor.objects.filter(id=myid)
    return render(request, "RasaChatbot.html", {'doctor': doctor[0]})

    # docts = Doctor.objects.all()
    # return render(request,"profile.html", {'docts': docts})
@login_required(login_url='login')
def bookpage(request,myid):
    doctor= Doctor.objects.filter(id=myid)
    return render(request, "book.html", {'doctor': doctor[0]})
@login_required(login_url='login')
def doctor_profile(request,myid):
    doctor= Doctor.objects.filter(id=myid)
    return render(request, "doctor_profile.html", {'doctor': doctor[0]})


def datetime_picker(request):
    return render(request, "datetime-picker.html")

    # doctor = Doctor.objects.filter(id=myid)
    # return render(request, "datetime-picker.html", {'doctor': doctor[0]})
    #doctor = Doctor.objects.filter(id=myid)
    #return render(request, "datetime-picker.html",{'doctor': doctor[0]})



@login_required(login_url='login')
def book(request,myid):
    doctor = Doctor.objects.filter(id=myid)

    if request.method=="POST":
        Doctor_name=request.POST['doctor_name']
        Department = request.POST['department']
        First_name = request.POST['fname']
        Last_name = request.POST['lname']
        Email = request.POST['email']
        Phone_number= request.POST['phone']
        Adress = request.POST['adress']
        Date_and_time= request.POST['date_time']
        user_id = request.POST['user_id']

        book = Appointment(Doctor_name=Doctor_name,Department=Department,First_name = First_name,Last_name=Last_name,Email=Email,Phone_number=Phone_number,Adress=Adress,Date_and_time=Date_and_time,user_id=user_id)
        book.save()

        e_subject = "Booking Confirmed!"
        e_msg = "Thankyou for booking ! your booking has been confirmed"
        e_mail = settings.EMAIL_HOST_USER

        send_mail(
            e_subject,
            e_msg,
            e_mail,
            [Email]

        )
        thank = True


        return render(request,'Sucess.html')

        #return render(request, 'index.html', {'thank': thank, 'id': id})

    users = User.objects.all()
    return render(request, 'index.html',{'doctor':doctor,'users':users})
    # return render(request,"datetime-picker.html",{"message": "You have book your Appointment with Dr. Kiran Bhusal, we will sent you confirmation mail"},{'doctor': doctor[0]})

@unauthenticated_user
def user_login(request):
    if request.user.is_authenticated:
        return redirect('doctors')
    else:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('doctors')

            else:
                messages.error(request,'Username and password didnot match')

        context = {}
        return render(request,'login.html', context)



def register(request):
    if request.user.is_authenticated:
        return redirect('doctors')
    else:
        form = CreateUserForm()

        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                username = form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ '' + username)

                return redirect('login')

        context = {'form':form}
        return render(request,'register.html',context)


def logoutUser(request):
    auth.logout(request)
    return redirect('/')

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['patient'])
# def appointments(request):
#     appointments = Appointment.objects.all()
#     context = {'appointments':appointments}
#     return render(request,"history.html",context)

@login_required(login_url='login')
def b_history(request, id = None):
    details = Appointment.objects.filter(user_id=id)
    return render(request,"history.html",{'details': details})

@login_required(login_url='login')
def b_history1(request, id = None):
    details = Appointment.objects.filter(user_id=id)
    return render(request,"io.html",{'details': details})

