from operator import is_
from django.shortcuts import redirect, render
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import Service



# Create your views here.

def home(request):
    services  = Service.objects.all()

    return render(request, 'myapp/index.html', {'services':services})

def register(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already Used')
                return redirect('register.html')
            
            else :
                user = User.objects.create_user(username=username, email=email, password=password2)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')

    else:        
        return render(request, 'myapp/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        # User is authenticated

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'myapp/login.html')


def portfolio(request):
    return render (request, 'myapp/portfolio.html')


def inner_page(request):
    return render (request, 'myapp/inner_page.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
