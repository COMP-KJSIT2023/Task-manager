from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Project, Supervisor, Tasks
from django.contrib.auth.models import User

@login_required
def home(response):
    current_user = response.user
    current_supervisor = Supervisor.objects.get(name=current_user.username)
    projects = Project.objects.filter(supervisor=current_supervisor)
    project_data = []
    for project in projects:
        username = User.objects.get(id=project.user_id).username
        project_data.append({'project': project, 'username': username})
    return render(response, "supervisor/home.html", {'projects': project_data})

@login_required
def index(response,pk):
    project = Project.objects.get(id=pk)
    current_user = project.user_id
    tasks = Tasks.objects.filter(user_id = current_user)
    
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("add"):
            id = response.POST.get("id")
            task = Tasks.objects.get(id=id)
            current_progress = task.progress
            new_progress = current_progress + 10
            task.progress = min(100, new_progress)
            task.save() 
        elif response.POST.get("delete"):
            id = response.POST.get("id")
            task = Tasks.objects.get(id=id)
            task.delete() 
        return redirect('index', pk)
    return render(response, "supervisor/index.html", {"tasks":tasks})