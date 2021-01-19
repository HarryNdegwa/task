from django.urls import path

from .views import *
from .api_views import *


urlpatterns = [
    path("login/",LoginView.as_view(),name="login"),
    path("logout/",logout_view,name="logout"),
    path("register/",SignUpView.as_view(),name="register"),
    path("user/admin/",AdminView.as_view(),name="admin"),
    path("admin/view/user/<int:id>/",AdminViewUser.as_view(),name="admin_view_user"),
    path("admin/create/user/",AdminCreateUserView.as_view(),name="admin_create_user"),
    path("admin/edit/user/<int:id>/",AdminEditUserView.as_view(),name="admin_edit_user"),
    path("admin/delete/user/<int:id>/",AdminDeleteUserView.as_view(),name="admin_delete_user"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("home/",HomeView.as_view(),name="home"),
    path("api/login/",SignInView.as_view(),name="sign_in"),
    path("api/register/",CreateUserView.as_view(),name="api_register"),
    path("api/profile/",UserProfileView.as_view(),name="api_profile")
]