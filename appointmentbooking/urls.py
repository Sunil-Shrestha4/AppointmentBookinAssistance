from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("login", views.user_login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logoutUser, name="logout"),
    path("history/<int:id>", views.b_history, name="history"),
    path("doctors",views.doctors, name="doctors"),
    path("about",views.about, name="about"),
    path("login",views.login, name="login"),
    path("contact",views.contact, name="contact"),
    path("bookpage/<int:myid>/",views.bookpage, name="bookpage"),
    path("doctor_profile/<int:myid>/",views.doctor_profile, name="bookpage"),
    path("bookpage/<int:myid>/book",views.book, name="book"),
    path("doctor_profile/<int:myid>/book",views.book, name="book"),
    path ("search/",views.search, name="search"),
    path ("doctor_profile/<int:myid>/doctors",views.doctors,name="doctors"),




]