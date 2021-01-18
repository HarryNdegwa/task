from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login,logout

from .forms import RegisterForm,UserUpdateForm

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
            return redirect("/home/")
        return render(request,self.template_name,{"error":True})



    def check_if_email(self,e):
        if "@" in e:
            return True
        return False



class SignUpView(View):

    template_name = "register.html"

    def get(self,request):
        form = RegisterForm()
        return render(request,self.template_name,{"form":form})


    def post(self,request):
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect("/login/")
        return render(request,self.template_name,{"form":form})



class ProfileEditView(View):

    template_name = "profile_edit.html"

    def get(self,request):
        form = UserUpdateForm()
        return render(request,self.template_name,{"form":form})
        




class AdminView(View):

    template_name = "admin.html"

    def get(self,request):
        return render(request,self.template_name,{})



class HomeView(View):

    template_name = "home.html"

    def get(self,request):
        return render(request,self.template_name,{})



def logout_view(request):
    logout(request)
    return redirect("/login/")
