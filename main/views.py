from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from .models import Tasks
from django.contrib.auth.models import User
from django.utils import timezone


# Create your views here.

@login_required
def home(response):
    current_user = response.user
    tasks = Tasks.objects.filter(user = current_user)
    
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("add"):
            id = response.POST.get("id")
            task = Tasks.objects.get(id=id)
            current_progress = task.progress
            new_progress = current_progress + 10
            task.progress = min(100, new_progress)
            task.save() 
            return redirect('/')
        elif response.POST.get("delete"):
            id = response.POST.get("id")
            task = Tasks.objects.get(id=id)
            task.delete() 
            return redirect('/')
    return render(response, "main/home.html", {'user': User, 'tasks':tasks})

@login_required
def create(response):
    if response.POST.get("newItem"):
        n1 = response.POST.get("newtaskhead")
        n2 = response.POST.get("newtaskbody")
        d = response.POST.get("deadline")
        response.user.tasks_set.create(deadline = d, task_heading = n1, task_details = n2, progress = 0.0, timestamp = timezone.now())
        return redirect('/')
    return render(response, "main/create.html", {"user":User})

@login_required
def notif(response):
    return render(response, "main/Notif.html", {})