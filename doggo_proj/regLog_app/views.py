from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt


def index(request):
    return render(request,'login.html')

def register(request):
    errors= User.objects.basic_validator(request.POST)
    if len(errors)> 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],email=request.POST['email'],
            password=pw_hash)
        messages.error(request, "Account already exists, please log in to the right")

       
        return redirect('/')

def login(request):
    users= User.objects.filter(email = request.POST['email'])
    if len(users) != 1:
        messages.error(request, 'No user with this email in database')
        return redirect('/')
    
    user = users[0]

    if not bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
        messages.error(request,'password does not match')
        return redirect('/')
    
    request.session['user_id'] = user.id
    request.session['user_email']= user.email
    request.session['user_first_name']= user.first_name
    return redirect('/success')

def success(request):

    if not 'user_id' in request.session:
        messages.error(request,'please log in to view this page')
        return redirect('/')
    
    return redirect('/jobs')

def logout(request):
    del request.session['user_id']
    del request.session['user_email']
    del request.session['user_first_name']

    return redirect('/')



