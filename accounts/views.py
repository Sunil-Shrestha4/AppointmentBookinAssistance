from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

from django.db import IntegrityError
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect("/")
#
#         else:
#             messages.info(request,'Your user name and password doesnot match!')
#             return redirect('login')
#     else:
#         return render(request,"login.html")
#
#
# def register(request):
#
#     if request.method == 'POST':
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#
#         if User.objects.filter(username=username).exists():
#             messages.info(request,'user name already taken')
#             return redirect('register')
#
#         elif User.objects.filter(email=email).exits():
#             messages.info(request, 'email3'
#                                    ' already taken')
#             return redirect('register')
#
#         else:
#             user = User.objects.create_user(username = username, first_name=first_name, last_name=last_name, email = email,password=password)
#             user.save();
#             print('user created')
#             return redirect('login')
#     else:
#         return  render(request,'register.html')
#
#
#
