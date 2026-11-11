from django.shortcuts import render, redirect
from sokoapp.models import *

# Create your views here.

def error(request):
    return render(request, '404.html')

def details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def index(request):

    if request.method == 'POST':
        myContact = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],

        )
        myContact.save()
        return redirect('/')
    else:
        return render(request, 'index.html')

    

def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')







