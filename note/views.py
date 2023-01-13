from django.shortcuts import render,redirect
from .models import Note,Reply
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
#-----------------------------------------------------------------------------------------------
# INDEX PAGE , 페이징 기능 구현

def index(req):
    pg = req.GET.get("page", 1)
    b = Note.objects.all()

    cate = req.GET.get("cate","")
    ss = req.GET.get("ss","")

    if ss:
        if cate =="sub":
            b = Note.objects.filter(subject__startswith=ss)
        elif cate == "wri":
            try:
                from main.models import User
                u = User.objects.get(username=ss)
                b = Note.objects.filter(writer=u)
            except:
                b = Note.objects.none() #아무것도 없는 레코드 설정시 적용
                

        elif cate =="con":
            b = Note.objects.filter(content__contains=ss)
        else:
            b = Note.objects.all()
    else:
        b = Note.objects.all()

    b = b.order_by('-pubdate')

    pag =Paginator(b,11)
    obj = pag.get_page(pg)

    context = {
        "bset" :obj,
        "ss" : ss,
        "cate": cate
    }

    return render(req, "note/index.html", context)

# CRUD ------------------------------------------------------------------------------------------
def show(req,bpk):

    b = Note.objects.get(id=bpk)
    r = b.reply_set.all()
    context = {

        "b" : b,
        "rset" : r

    }
    return render(req,'note/show.html',context)

def delete(req,bpk):
    b = Note.objects.get(id=bpk)
    if b.writer == req.user:
        b.delete()
    else:
        messages.error(req,"Invalid Connection")
    return redirect("note:index")

def create(req):
    
    if req.method == "POST":
        s = req.POST.get("sub")
        c = req.POST.get("con")
        if s == None:
            messages.error(req, "subject error")
        elif c == None:
            messages.error(req,"content error")
        else:
            Note(subject=s, writer=req.user, content=c, pubdate=timezone.now()).save()
            return redirect("note:index")
    return render(req, "note/create.html")

def update(req,bpk):
    b = Note.objects.get(id=bpk)

    if b.writer != req.user:        # 글작성자와 업데이트 작성자가 같지 않다면
        messages.error(req,"Invalid Connection")
        return redirect("note:index")

    if req.method == "POST":
        s = req.POST.get("sub")
        c = req.POST.get("con")
        b.subject = s
        b.content = c
        b.save()
        messages.success(req, "수정되었습니다.")
        return redirect("note:index")
    context = {

        "b" : b

    }
    return render(req,"note/update.html",context)
# Create your views here.

# 좋아요 기능 구현

def likey(req,bpk):
    b = Note.objects.get(id=bpk)
    b.likey.add(req.user)

    return redirect("note:show",bpk)

def unlikey(req,bpk):
    b = Note.objects.get(id=bpk)
    b.likey.remove(req.user)

    return redirect("note:show",bpk)


#댓글 기능 구현
def creply(req,bpk):
    b = Note.objects.get(id=bpk)
    c = req.POST.get('com')
    Reply(board=b,replyer=req.user,comment=c).save()

    return redirect("note:show",bpk)



def dreply(req,bpk,rpk):
    r = Reply.objects.get(id=rpk)
    if r.replyer == req.user:    
        r.delete()
    else:
        messages.error(req, "Invalid connection")
    return redirect("note:show",bpk)