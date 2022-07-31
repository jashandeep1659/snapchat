from django.urls import path
from .views import *

urlpatterns = [
    path("", Home, name="Home"),
    path("login/", Login, name="Login"),
]
