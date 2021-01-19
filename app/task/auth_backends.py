from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

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



class PhoneAuthBackend(BaseBackend):

    def authenticate(self,request,phone=None,password=None):
        try:
            user = User.objects.get(phone=phone)
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



class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):

        """
            authenticate the request and return a user and token tuple    
        """
        auth_header = request.headers.get("Authorization")
        if auth_header:
            _,token = auth_header.split(" ")
            if token:
                res = User.decode_auth_token(token)
                if type(res) == int:
                    user = User.objects.get(id=res)
                    if user:
                        return (user,None)
                else:
                    raise AuthenticationFailed(res)     
            else:
                raise AuthenticationFailed("Invalid Token")
        raise AuthenticationFailed("Invalid Token")



    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


    def authenticate_header(self,request):
        return "Token"


