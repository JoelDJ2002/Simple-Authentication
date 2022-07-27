import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# admin - jowell
# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request,'dashboard.html', {'fname':fname})
        else:
          messages.error(request, "Bad Credentials!! Please refresh and login again with correct credentials.")
          return redirect('/signin')

    return render(request, 'signin.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname'] 
        email = request.POST['email']
        pass1 = request.POST['pass1']

        if User.objects.filter(username=username):
            messages.error(request,"Username already in use. Please try another one")
            return redirect('/signup')

        if User.objects.filter(email=email):
            messages.error(request,"Email already in use. Please try another one")
            return redirect('/signup')

        



        user = User.objects.create_user(username, email, pass1)
        user.fname = fname
        user.save()
        messages.success(request, "Your account has been successfully created")

        return redirect('signin')
      
   
       
    
    return render(request, 'signup.html')


def dashboard(request):
    return render(request, 'dashboard.html')

    
def signout(request):
   logout(request)
   return redirect('index')

def about(request):
    return render(request, 'portfolio.html')