from django.shortcuts import render, redirect
from .forms import Registerform
from main.models import Supervisor, Project
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm
import string, random

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

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
    return render(response, "register.html", {"form":form})