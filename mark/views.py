from django.shortcuts import redirect, render
from .models import Book
from django.contrib import messages
# Create your views here.

def index(req):
    b = req.user.book_set.all()
    context = {
        "bset" : b
    }
    return render(req, "mark/index.html",context)

def create(req):
    if req.method == "POST":
        im =req.POST.get("impo")
        sn =req.POST.get("sname")
        su =req.POST.get("surl")
        sc =req.POST.get("scon")
        Book(site_name=sn, site_url=su, site_con=sc, impo=bool(im), maker=req.user).save()
        return redirect("mark:index")
    return render(req, "mark/create.html")

def delete(req,bpk):
    b = Book.objects.get(id=bpk)
    b.delete()
    messages.success(req,"삭제되었습니다")
    return redirect("mark:index")