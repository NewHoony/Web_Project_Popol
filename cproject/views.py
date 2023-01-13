from django.shortcuts import render,redirect
from .models import Project,Image
from main.models import User
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages

def index(req):
    pg = req.GET.get("page", 1)
    p = Project.objects.all()

    cate = req.GET.get("cate","")
    ss = req.GET.get("ss","")

    if ss:
        if cate =="pro":
            p = Project.objects.filter(project__startswith=ss)
        elif cate == "mak":
            try:
                from main.models import User
                u = User.objects.get(username=ss)
                p = Project.objects.filter(maker=u)
            except:
                p = Project.objects.none() #아무것도 없는 레코드 설정시 적용
                

        elif cate =="con":
            p = Project.objects.filter(content__contains=ss)
        else:
            p = Project.objects.all()
    else:
        p = Project.objects.all()

    p = p.order_by('-pubdate')

    pag =Paginator(p,11)
    obj = pag.get_page(pg)
    
    context = {
        "pset" :obj,
        "ss" : ss,
        "cate": cate
    }

    return render(req, "cproject/index.html",context)

def show(req,ipk):
    project = Project.objects.get(id=ipk)
    ph = project.image_set.all()
    context = {
        "pro" : project,
        "phset" : ph
    }

    return render(req,"cproject/show.html",context)

def create(req):
    if req.method == "POST":
        pro = req.POST.get("pro")
        c = req.POST.get("con")
        t = req.POST.get("tech")
        cp = req.FILES.getlist("cpic")
        cc = req.POST.getlist("ccon")
        p = Project(project=pro, content=c, tech=t, maker=req.user, pubdate=timezone.now())
        p.save()
        for pic, con in zip(cp,cc):
            Image(project=p, pic=pic, con=con).save()
        
        return redirect("cproject:index")       
    return render(req, "cproject/create.html")

def delete(req,ipk):
    project = Project.objects.get(id=ipk)
    if project.maker == req.user:
        project.delete()
    else:
        messages.error(req, "작성자가 아니면 삭제 할 수 없습니다.")
    return redirect("cproject:index")

def update(req,ipk):
    project = Project.objects.get(id=ipk)

    if project.maker != req.user:        # 글작성자와 업데이트 작성자가 같지 않다면
        messages.error(req,"작성자가 아니면 수정 할 수 없습니다.")
        return redirect("cproject:index")

    if req.method == "POST":
        pro = req.POST.get("pro")
        c = req.POST.get("con")
        project.project = pro
        project.content = c
        project.save()
        return redirect("cproject:index")
    context = {

        "pro" : project

    }
    return render(req,"cproject/update.html",context)

# Create your views here.
