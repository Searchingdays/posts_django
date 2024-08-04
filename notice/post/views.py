from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import msg, comment
from django.template import loader
from django.http import Http404
from django.db.models import F
from django.urls import reverse
from django.template import Template
from django.contrib.auth import authenticate





def index(request):
    r = msg.objects.order_by("id")
    m ={}
    #rlist = ",".join([i.msg_title for i in r ])
    rlist = list(r)
    #for i in rlist:
       # m = m + {}
    context ={
        "all_posts":rlist,
        "post_num":m
    }
    return render(request,"post/index.html", context)


def content(request, msg_id):
    m = msg.objects.get(pk=msg_id)
    id = m.id
    context ={
        "content":m.msg_text,
        "msg_title":m.msg_title,
        "msg_id": id,
        "date":m.msg_date

    }
    
    return render(request,"post/content.html", context )

def like(request, msg_id, press=False):
    post = list(msg.objects.all())
    m = msg.objects.get(pk=msg_id)
    num = m.msg_like
    if (press is True):
        num = num+1
    

    #n = len(post)
    #for p in range(n):
     #   m[p] = msg.objects.get(pk=post.index(p)+1) 
    context ={
        "j": m.id,
        "num":num,
        "post_title":m.msg_title,
        "posts":post
    }
    return render(request, "post/likes.html", context)

def likepress(request, msg_id):
    m = msg.objects.get(pk=msg_id)
    if request.method == 'POST':
        l = request.POST.get("l")
        
    #num = msg.objects.get(pk=request.POST["msg_like"])
    num = m.msg_like
    num = F("num") +1
    #num.save()
    return HttpResponseRedirect(reverse( "post:like", args=m.id))


def comments(request, msg_id):
    m = msg.objects.get(pk=msg_id)
    c = comment.objects.filter(post = m)
    context ={
        "comments":c,
        "post_title":m.msg_title,
        "date":m.msg_date,
        "msg_id":m.id

    }
    return render(request, "post/comments.html", context)

def comment_write(request, msg_id):
    m = msg.objects.get(pk=msg_id)
    c = comment()

    context = {
            "date":m.msg_date,
            "post_title":m.msg_title
    }

    if request.method == 'POST':
        text = request.POST.get('textfield', None)
        c.comment_text = text
        c.post = m
        c.save()

        
        return HttpResponse(text +"comment saved")
    else:
        return render(request, "post/comments.html", context)




    
    

def text(request, msg_id):
    try:
        m = msg.objects.get(pk=msg_id)
    except msg.DoesNotExist:
        raise Http404("msg does not exist")
    return render(request, "post/text.html",{"msg":m})

def auth(request, username, password):
    user = authenticate(username, password)
    if user is not None:
        pass
    else:
        pass
    context = {
        "uname":username,
        "pword":password
    }
    return render(request, "post/auth.html", context )


    

# Create your views here.
