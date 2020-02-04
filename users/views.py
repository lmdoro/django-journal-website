from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, EmailChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success (request,f'Your account has been created. You may now log in, {username}!')
            return redirect ('login')
            
    else:
        form = RegistrationForm()  
    
    context = {
        'form':form,
        'title':'Sign up'
    }
    
    return render(request, 'users/register.html', context)

def u_login(request):
    form = LoginForm()
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error (request, 'Invalid credentials!')
            return redirect('login')
    
    context = {
        'form':form,
        'title':'Log in'
    }

    return render(request, 'users/login.html', context)

@login_required
def email_change(request):
    form = EmailChangeForm()
    if request.method == 'POST':
        form = EmailChangeForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['current_email'] !=request.user.email:
                messages.error(request, 'Invalid input!')
                return redirect('email_change')
            elif form.cleaned_data['email1'] == form.cleaned_data['email2']:
                user = User.objects.get(username=request.user)
                user.email = form.cleaned_data['email1']
                user.save()
                return redirect('email_change_done')
            else:
                messages.error(request, 'Invalid input!')
                return redirect('email_change')
    
    context = {'form':form,
    'title':'Change Email'}

    return render(request, 'users/email_change.html', context)

@login_required
def email_change_done(request):
    return render(request, 'users/email_change_done.html')


