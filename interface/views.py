from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registration

def home(request):
    return HttpResponse ("hello")

def index(request):
    return render(request, "interface/index.html")

def Registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        paddress = request.POST.get('paddress')
        taddress = request.POST.get('taddress')
        pnum = request.POST.get('pnum')
        dob = request.POST.get('dob')
        registration = Registration(
            name=name,
            paddress=paddress,
            taddress=taddress,
            pnum=pnum,
            dob=dob
        )
        registration.save()
    return render(request, "interface/Registration.html")

def Update(request):
    return render(request, "interface/Update.html")