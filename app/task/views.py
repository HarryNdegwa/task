from django.shortcuts import render,redirect
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
                return redirect("/admin/")
            return redirect("/home/")
        return HttpResponse({})



    def check_if_email(self,e):
        if "@" in e:
            return True
        return False



class AdminView(View):

    template_name = "admin.html"

    def get(self,request):
        return render(request,self.template_name,{})



class HomeView(View):

    template_name = "home.html"

    def get(self,request):
        return render(request,self.template_name,{})