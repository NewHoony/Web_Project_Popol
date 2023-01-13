from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages

def index(req):
    return render(req,"main/index.html")

def login_user(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(req,u)
            messages.success(req,f"{u} Welcome")
            return redirect("main:index")
        else:
            messages.error(req,"계정 정보 불일치")
    
    return render(req,"main/login.html")

def logout_user(req):
    logout(req)
    return redirect("main:index")

def signup(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        uc = req.POST.get("ucomn")
        pi = req.FILES.get("upic")  
        User.objects.create_user(username=un, password=up, comment=uc, pic=pi)
        return redirect("main:login")
    return render(req,"main/signup.html")

def profile(req):
    return render(req, "main/profile.html")

def delete(req):
    req.user.delete()
    return redirect("main:index")

def update(req):
    if req.method == "POST":
        u = req.user
        up = req.POST.get("upass")
        um = req.POST.get("umail")
        pi = req.FILES.get("upic")
        uc = req.POST.get("ucomn")       
        if up:
            u.set_password(up)
        if pi:
            u.pic = pi
        u.comment = uc
        u.email = um
        u.save()
        login(req,u)
        return redirect("main:profile")
    return render(req,"main/update.html")
# Create your views here.

