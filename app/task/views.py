from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login,logout,get_user_model

from .forms import RegisterForm,UserUpdateForm


User = get_user_model()

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



class ProfileView(View):

    template_name = "profile_edit.html"

    def get(self,request):
        initial_data = {
            "name":request.user.name,
            "email":request.user.email,
            "phone":request.user.phone,
            "role":request.user.role,
            "profile":request.user.profile
        }
        form = UserUpdateForm(initial=initial_data)
        return render(request,self.template_name,{"form":form})


    def post(self,request):
        form = UserUpdateForm(request.POST,request.FILES,instance=request.user)
        c = self.check_if_email_or_phone_changed(request.user,request.POST)
        if form.is_valid():
            form.save()
            if c:
                logout(request)
                return redirect("/login/")
            return redirect("/home/")
        return render(request,self.template_name,{"form":form})


    def check_if_email_or_phone_changed(self,user,data):
        if user.email != data.get("email"):
            return True
        elif user.phone != data.get("phone"):
            return True
        else:
            return False
        
    

class AdminView(View):

    template_name = "admin.html"

    def get(self,request):
        users = None
        if self.check_if_email(str(request.user)):
            users = User.objects.all().exclude(email = str(request.user))
        else:
            users = User.objects.all().exclude(phone = str(request.user))     
        return render(request,self.template_name,{"users":users})



    def check_if_email(self,e):
        if "@" in e:
            return True
        return False


class AdminActionsView(View):

    template_name = "admin_add_user.html"

    def get(self,request):
        form = RegisterForm()
        return render(request,self.template_name,{"form":form})



class HomeView(View):

    template_name = "home.html"

    def get(self,request):
        return render(request,self.template_name,{"user":request.user})



def logout_view(request):
    logout(request)
    return redirect("/login/")
