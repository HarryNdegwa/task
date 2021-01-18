from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        exclude = ["is_staff","is_active"]