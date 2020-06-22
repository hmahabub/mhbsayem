from django.shortcuts import render, redirect
from .models import *


def home_page(request):
    spec = specifics.objects.all()
    serv = service.objects.all()
    bas = basic.objects.all()
    b_price = basic_price.objects.get(id=1)
    pre = basic.objects.all()
    p_price = premium_price.objects.get(id=1)
    return render(request, "home.html", {"specifics":spec, "service":serv, "basic":bas,"b_price":b_price,"p_price":p_price, "premium":pre})

def portfolio(request):
    project = projects.objects.all()
    return render(request, "portfolio.html",{'projects':project})

def save(request):
    if request.method =="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        msg = request.POST["message"]
        a_msg = message(name=name, email=email, message=msg)
        a_msg.save()
        return redirect("/")

def messages(request):
    msg = message.objects.all()
    return render(request, "message.html", {"message": msg})

# Create your views here.
