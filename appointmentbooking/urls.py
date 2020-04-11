from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    #path("login",views.login,),
    # path("register",views.register,)
    path("doctors",views.doctors, name="doctors"),
    path("departments",views.departments, name="departments"),
    path("about",views.about, name="about"),
    path("elements",views.elements, name="elements"),
    path("blog-details",views.blog_details, name="blog-details"),
    path("blog-home",views.blog_home, name="blog-details"),
    path("contact",views.contact, name="contact"),
    path("abc/<int:myid>/",views.view_profile, name="view_profile"),
    path("datetime-picker",views.datetime_picker, name="datetime_picker"),
    #path("book",views.book, name="book")




]