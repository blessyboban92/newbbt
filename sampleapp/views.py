from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,AbstractUser
from . models import Services
#from django.http import HttpResponse
def demo(request):
    obj=Services.objects.all()
    return render(request,'index.html',{'result':obj})
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'customer.html')
        else:
            error="Invalid credentialal"
            return render(request,'login.html',{'error':error})
    else:
        return render(request,'login.html')

def registerf(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                error="Alreay existed user"
                return render(request,'register.html',{'error':error})
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("user created")
                messages.success(request,'Registration Successfully Done!')
                return redirect('login')
        else:
            error ="Password doesn't match,Please enter your password again "
            return render(request,'register.html',{'error':error})
    else:
        return render(request,'register.html')
def customerf(request):
    return render(request,'customer.html')