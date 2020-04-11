from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

from django.db import IntegrityError
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("doctors")

        else:
            messages.info(request,'invqlie credentials')
            return redirect('login')
    else:
        return render(request,"login.html")


def register(request):

    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        # confirm_password = request.POST['confirm_password']
        #
        # if password == confirm_password:
        #     if User.objects.filter(username=user_name).exists():
        #         print('Username taken')
        #     elif User.objects.filter(email=email).exists():
        #         print('email taken')
        #
        #     else:
        user = User.objects.create_user(username = user_name, first_name=first_name, last_name=last_name, email = email,password=password)
        user.save();
        print('user created')
        return redirect('login')
    else:
        return  render(request,'register.html')