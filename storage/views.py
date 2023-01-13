from django.shortcuts import render,redirect
from .models import Project,File
from django.contrib import messages


def index(req):
    p = Project.objects.all()
    context ={
        "pro" : p
    }

    return render(req, "storage/index.html",context)

def upload(req):
    if req.method == "POST":
        pro = req.POST.get("pro")
        c = req.POST.get("con")
        cf = req.FILES.getlist("cfile")
        cc = req.POST.getlist("ccon")
        p = Project(project=pro, content=c, uploader=req.user)
        p.save()
        for file,con in zip(cf,cc):
            File(project=p, file=file, con=con).save()
        
        return redirect("storage:index")  


    return render(req, "storage/upload.html")

def show(req,ipk):
    project = Project.objects.get(id=ipk)
    fi = File.objects.filter(project=project)
    context = {
        "pro" : project,
        "fiset" : fi
    }

    return render(req,"storage/show.html",context)

def delete(req,ipk):
    p = Project.objects.get(id=ipk)
    p.delete()
    messages.success(req,"삭제되었습니다")
    return redirect("storage:index")




# Create your views here.
