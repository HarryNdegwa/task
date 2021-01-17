from django.urls import path

from .views import *


urlpatterns = [
    path("login/",LoginView.as_view(),name="login"),
    path("admin/",LoginView.as_view(),name="admin"),
    path("home/",LoginView.as_view(),name="home")
]