from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()


class EmailAuthBackend(BaseBackend):

    def authenticate(self,request,email=None,password=None):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        else:
            password_valid = check_password(password,user.password)
            if not password_valid:
                return None
            return user


    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
