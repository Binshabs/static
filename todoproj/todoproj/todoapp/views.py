from django.shortcuts import render
from .models import Task

# Create your views here.


def Home(req):
    tasks=Task.objects.all()
    if req.method=="POST":
        task=req.POST.get('task','')
        priority=req.POST.get('prority','')
        todo=Task(task=task,priority=priority)
        todo.save()
    
    return render(req,'index.html',{"tasks":tasks})

def Update(req,id):
    tasks=Task.objects.get(id=id)
    if req.method=="POST":
     task=req.POST.get('task','')
     priority=req.POST.get('prority','')
    
    # print(id)
    Task.objects.get(id=id)
    return render(req,'update.html',{"task":task})

    


# def Home(req):
#      return render(req,"index.html")
    


# def contact(req):
#     return render(req,"contact.html")