from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from mainApp.models import UserModel
from django.contrib import messages
from django.contrib import auth
from random import randint
from django.core.mail import send_mail,send_mass_mail

def HomePage(request):
    return render(request, 'index.html')

def DashBoardPage(request):
    return render(request, 'dashboard.html')

def SignupPage(request):
    if request.method=="POST":
        u=UserModel()
        u.name = request.POST.get("name")
        uname = u.username = request.POST.get("username")
        pward = request.POST.get("password")
        u.email = request.POST.get("email")
        u.phone = request.POST.get("phone")
        u.city = request.POST.get("city")
        user = User.objects.create_user(username=uname,password=pward)
        u.save()
        messages.success(request, 'You account create successfully ')
    return render(request, 'signup.html')

def LoginPage(request):
    if not request.user.is_authenticated:
        if(request.method=="POST"):
            uname = request.POST.get('username')
            pward = request.POST.get('password')
            user = authenticate(username=uname,password=pward) 
            if(user is not None):
                return HttpResponseRedirect('/dashboard/') 
        return render(request, 'login.html')
    else:
        return HttpResponseRedirect('/dashboard/')

def LogoutPage(request):
    logout(request)
    return HttpResponseRedirect('/')

def ForgetPasswordPage(request):
    if(request.method=="POST"):
        flag = False
        username = request.POST.get("username")
        user = UserModel.objects.get(username=username)
        flag=True
        if(flag==True):
            user.otp = randint(1000,9999)
            user.save()
            subject = "OTP for Password Reset"
            body =  """
                        Hello!!!!
                        Your OTP for PasssWord Rest is
                        {}
                        Team:   Karma
                    """.format(user.otp)
            send_mail(subject, body,"armannmalik9880@gmail.com",[user.email,], fail_silently=False)
            return HttpResponseRedirect('/enterotp/'+username+"/")
        else:
            messages.error(request,"User Name not fund")
    return render(request, 'forgetpassword.html')

def enterotp(request,username):
    if(request.method=="POST"):
        flag = False
        otp = int(request.POST.get("otp"))
        user = UserModel.objects.get(username=username)
        flag=True
        if(flag==True):
            if(user.otp==otp):
                return HttpResponseRedirect('/resetpassword/'+username+"/")
            else:
                messages.error(request,"OTP Does't Match")    
        else:
            messages.error(request,"User Name not fund")
    return render(request, 'enterotp.html')

def resetPassword(request,username):
    if(request.method=="POST"):
        password1 = request.POST.get("p1")
        password2 = request.POST.get("p2")
        # try:
        user = User.objects.get(username=username)
        if(password1==password2):
            user.set_password(password1)
            user.save()
            subject = "Password Reset"
            body =  """
                       Your Password Reset
                       successfully.New 
                       password genereted
                        
                        Team:   Asheesh
                    """
            send_mail(subject, body,"armannmalik9880@gmail.com",[user.email,], fail_silently=False)
            return HttpResponseRedirect('/login/')
        else:
            messages.error("Password and Confirm Password not Match")
        # except:
        #     messages.error(request,"User not fund")
    return render(request,"resetpassword.html")
