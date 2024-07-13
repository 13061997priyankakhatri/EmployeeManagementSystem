from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
    context = {
        'variable' : '"This is context block."'
    }
    return render(request ,"index.html", context)

def about(request):
    return render(request ,"about.html")

def services(request):
    if request.method == "POST":
        address = request.POST.get('address')
        salary = request.POST.get('salary')
        city = request.POST.get('city')
        state = request.POST.get('state')
        union_territories = request.POST.get('union_territories')
        pincode = request.POST.get('pincode')
        service = Service(address=address, salary=salary, city=city, state=state, union_territories=union_territories, pincode=pincode)
        service.save()
        messages.success(request, "Your data added successfully!!")
    return render(request ,"services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = request.POST.get('contact')
        phone = Contact(name=name, email=email, desc=desc, contact=contact, date=datetime.today())
        phone.save()
        messages.success(request, "Your message has been sent!!")
    return render(request ,"contact.html")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Login(username=username, password=password, email=email)
        user.save()
        messages.success(request, "Your login request approved successfully!!")
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')