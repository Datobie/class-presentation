from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page, name="home"),
    path("about/", about_page, name="about"),
    path("course/", course_page, name="courses"),
    path("contact/", Contact, name="contact")
]