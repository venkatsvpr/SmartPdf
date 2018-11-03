from django.shortcuts import render,HttpResponse
from django.template import loader


# Create your views here.

def index(request):
    return render(request,"index.html")
