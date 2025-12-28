from django.shortcuts import render
from . models import *

def home(request):
          products=Product.objects.filter(trending=1)
          return render(request,"shop/index.html",{"products":products})

def register(request):
          return render(request,"shop/register.html")

def collections(request):
          catagory=Catagory.objects.filter(status=0)
          return render(request,"shop/collections.html",{"catagory":catagory})
