from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

    





def Home(req):
     return render(req,"index.html")
    


def form(req):
    return render(req,"form.html")