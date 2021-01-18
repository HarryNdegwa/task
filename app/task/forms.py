from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["name","email","phone","role","profile","password1","password2"]




class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ["name","email","phone","role","profile"]