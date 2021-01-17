from django.shortcuts import render
from django.views import View

class LoginView(View):

    template_name = "login.html"

    def get(self,request):
        pass



    def post(self,request):
        pass
