from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from home.models import Contact
from datetime import datetime



# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this my webpage")

def about(request):
    #return HttpResponse("this my about")
    return render(request, 'about.html')

def services(request):
    #return HttpResponse("this my services") 
    return render(request, 'service.html') 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
    return render(request, 'contact.html')

