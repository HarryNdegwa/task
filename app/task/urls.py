from django.urls import path

from .views import *


urlpatterns = [
    path("login/",LoginView.as_view(),name="login"),
    path("logout/",logout_view,name="logout"),
    path("user/admin/",AdminView.as_view(),name="admin"),
    path("home/",HomeView.as_view(),name="home")
]