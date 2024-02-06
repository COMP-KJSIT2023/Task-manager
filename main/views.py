from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tasks, User
from django.utils import timezone

# Create your views here.
def home(response):
    user = User.objects.get(id=1)
    tasks = Tasks.objects.filter(user=user)
    
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
    return render(response, "main/home.html", {'user': user, 'tasks':tasks})

def create(response):
    user = User.objects.get(id=1)
    if response.POST.get("newItem"):
        n1 = response.POST.get("newtaskhead")
        n2 = response.POST.get("newtaskbody")
        d = response.POST.get("deadline")
        user.tasks_set.create(deadline = d, task_heading = n1, task_details = n2, progress = 0.0, timestamp = timezone.now())
    return render(response, "main/create.html", {"user":user})