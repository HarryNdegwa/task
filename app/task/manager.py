from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError(_('Email is required!'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email, password, **extra_fields):
        extra_fields.setdefault('role', "admin")
        return self.create_user(email,password,**extra_fields)
    