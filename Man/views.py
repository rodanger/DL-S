import email
from multiprocessing import context
from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,'Man/index.html')

def about(request):
    return render(request,'Man/about.html')


def contact(request):
    if request.method == 'POST':
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact.name=name
        contact.email=email
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACT US</h1>")

    return render(request,'Man/contact.html')



def gallery(request):
    return render(request,'Man/galia.html')