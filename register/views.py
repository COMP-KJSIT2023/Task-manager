from django.shortcuts import render, redirect
from .forms import Registerform, LoginForm
from main.models import Supervisor
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
import string, random

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def has_permission(user):
    user = User.objects.get(username=user)
    return  user.groups.filter(name='Supervisor').exists()

def register(response):
    if response.method == "POST":
        form = Registerform(response.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Normal User')
            user.groups.add(group)
        supervisor = Supervisor.objects.get(code=response.POST.get("Supervisor"))
        user = User.objects.get(username=response.POST.get("username"))
        name = response.POST.get("Project")
        supervisor.project_set.create(name = name, user=user) 
        return redirect("/login")
    else:
        form = Registerform()
    return render(response, "registration/register.html", {"form":form})

def supervisor(response):
    if response.method == "POST":
        form = Registerform(response.POST) 
        if form.is_valid():
            user = form.save()
            name = user.username
            Supervisor.objects.create(name = name, code=generate_random_string(6).upper())
            group = Group.objects.get(name='Supervisor')
            user.groups.add(group)
        return redirect("/login")
    else:
        form = Registerform()
    return render(response, "registration/supervisor.html", {"form":form})

def login(response):
    if response.method == "POST":
        form = LoginForm(response.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(response, username=username, password=password)
            if user is not None:
                auth_login(response, user)
                if has_permission(user):
                    return redirect('/super/')
                else:
                    return redirect('/')
            else:
                return render(response, 'registration/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(response, "registration/login.html", {"form":form})