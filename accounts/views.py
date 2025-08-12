from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.db import IntegrityError
from feedback.models import Feedback
# Create your views here.
def home(request):
    return render(request,'home.html')


def signupaccount(request):
    
    if request.method=='GET':
        return render(request,'signupaccount.html',{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                login(request,user)
                user.save()
                return redirect('dashboard')
            except IntegrityError:
                return render(request,'signupaccount.html',{'form':UserCreationForm,'error':'Username already exists'})
        else:
            return render(request,'signupaccount.html',{'form':UserCreationForm,'error':'Passwords do not match'})
        
        
def loginaccount(request):
    if request.method=='GET':
        return render(request,'loginaccount.html',{'form':AuthenticationForm})
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        
        if user is None:
            return render(request,'loginaccount.html',{'form':AuthenticationForm,'error':'User doest not exist..Try again!!'})
        
        else:
            login(request,user)
            return redirect('dashboard')
        
def logoutaccount(request):
    logout(request)
    return redirect('home')

def show_feedback(request):
    feedbacks=Feedback.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'feedbacks': feedbacks})