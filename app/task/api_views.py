from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView
from django.contrib.auth import get_user_model,authenticate
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import permissions,status



class SignInView(APIView):

    permission_classes = (permissions.AllowAny,)

    authentication_classes = ()

    def post(self,request,format=None):
        pass