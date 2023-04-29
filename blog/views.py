from django.shortcuts import render,redirect,HttpResponse
from blog.models import user
from blog.models import contact
from blog.models import dform
from blog.models import customer,amount
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.conf import settings

def home(request):
    if request.method=='POST':
        if request.POST.get('email'):
            saverecord=customer()
            saverecord.email=request.POST.get('email')
            saverecord.save()
    return render(request,'index.html')  

def money(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('amount'):
            saverecord=amount()
            saverecord.name=request.POST.get('name')
            saverecord.email=request.POST.get('email')
            saverecord.amount=request.POST.get('amount')
            saverecord.save()
            messages.success(request,'Your submitted your donate form')
    return render(request,'money.html')
     

def signin(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1!=pass2:
            messages.success(request,"Your password and confirm password are not Same!!!")
            return redirect('signin')    
        else:
            saverecord=user()
            saverecord.name=request.POST.get('name')
            saverecord.email=request.POST.get('email')
            saverecord.pass1=request.POST.get('pass1')
            saverecord.pass2=request.POST.get('pass2')
            saverecord.save()
            my_user=user.objects.create_user(name,email,pass1)
            my_user.save()
            return redirect('login')  
              
    else:
         return render(request,'signin.html')
    
def log_in(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pass1=request.POST.get('pass1')
        user=authenticate(request,username=name,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.success(request,"Username or Password is incorrect!!!")
            return redirect('login')
    return render(request,'login.html')


def report(request):
    return render(request,'report.html')

def donate(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('mail') and request.POST.get('phone') and request.POST.get('dno') and request.POST.get('street') and request.POST.get('city') and request.POST.get('state') and request.POST.get('pin') and request.POST.get('food') and request.POST.get('time') and request.POST.get('quantity'):
            saverecord=dform()
            saverecord.name=request.POST.get('name')
            saverecord.mail=request.POST.get('mail')
            saverecord.phone=request.POST.get('phone')
            saverecord.dno=request.POST.get('dno')
            saverecord.street=request.POST.get('street')
            saverecord.city=request.POST.get('city')
            saverecord.state=request.POST.get('state')
            saverecord.pin=request.POST.get('pin')
            saverecord.food=request.POST.get('food')    
            saverecord.time=request.POST.get('time') 
            saverecord.quantity=request.POST.get('quantity')
            saverecord.save()
            messages.success(request,'Your submitted your donate form')
            if messages==True:
                return render(request, 'index.html')
        else:
            messages.error(request,'Your form is not submited')
    return render(request,'donate.html')
    


def contacts(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('comment'):
            saverecord=contact()
            saverecord.name=request.POST.get('name')
            saverecord.email=request.POST.get('email')
            saverecord.phone=request.POST.get('phone')
            saverecord.comment=request.POST.get('comment')
            saverecord.save()
            messages.success(request,'Submited your chat Sucessfully....')
            if messages==True:
                return render(request,'index.html')
        else:
            messages.error(request,'Your chat is not submited')
            return render(request,'contacts.html')
    return render(request,'contacts.html')

def about(request):
    return render(request,'about.html')

def donor(request):
    dforms=dform.objects.all()
    amounts=amount.objects.all()
    
    return render(request,'donor.html',{'dforms':dforms,'amounts':amounts})
    

    

def Logout(request):
    logout(request)
    return render(request,'login.html')

