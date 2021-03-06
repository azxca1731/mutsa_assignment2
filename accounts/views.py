from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or passord is no correct!\n try again!'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, 'signup.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('home')
    else:
        return render(request, 'login.html',{"error": "You can't not logout! cuz you're not in session!"})