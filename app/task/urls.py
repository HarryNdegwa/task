from django.urls import path

from .views import *


urlpatterns = [
    path("login/",LoginView.as_view(),name="login"),
    path("logout/",logout_view,name="logout"),
    path("register/",SignUpView.as_view(),name="register"),
    path("user/admin/",AdminView.as_view(),name="admin"),
    path("admin/actions/",AdminActionsView.as_view(),name="admin_add_user"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("home/",HomeView.as_view(),name="home")
]