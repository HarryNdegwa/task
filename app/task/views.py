from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login

class LoginView(View):

    template_name = "login.html"

    def get(self,request):
        return render(request,self.template_name,{})


    def post(self,request):
        primary = request.POST.get("primary")
        payload = {}
        if self.check_if_email(primary):
            payload["email"] = primary
            payload["password"] = request.POST.get("password")
        else:
            payload["phone"] = primary
            payload["password"] = request.POST.get("password")

        user = authenticate(request,**payload)

        if user:
            login(request,user)
            if user.role == "ADMIN":
                return HttpResponse({})
            return HttpResponse({})
        return HttpResponse({})



    def check_if_email(self,e):
        if "@" in e:
            return True
        return False