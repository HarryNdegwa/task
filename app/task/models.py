import datetime,jwt
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from cloudinary.models import CloudinaryField


from .manager import CustomUserManager

ROLE_CHOICES =(("USER","user"),("ADMIN","admin"))


class CustomUser(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20,unique=True)
    role = models.CharField(max_length=5,choices=ROLE_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    profile = models.CloudinaryField('image')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
        

    
    def encode_auth_token(self,user_id):
        try:
            payload = {        
                "exp":datetime.datetime.utcnow()+datetime.timedelta(days=30),
                "iat":datetime.datetime.utcnow(),
                "sub":int(user_id)
            }   
            return jwt.encode(payload,"\xd1\xd7\xee_\xab\xd0UB:\x18\x1bh8\xc8\x90\x0eb+\xc67R\xec^\x90",algorithm="HS256")

        except Exception as e:
            return e


    @staticmethod
    def decode_auth_token(token):
        try:
            payload = jwt.decode(token,"\xd1\xd7\xee_\xab\xd0UB:\x18\x1bh8\xc8\x90\x0eb+\xc67R\xec^\x90",algorithms=["HS256"])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Token expired! Please log in again."
        except  jwt.InvalidTokenError:
            return "Invalid Token! Please log in again."


    

