from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todolist, Item
from .forms import CreateNewList

# Create your views here.
def home(response):
    return render(response, "main/home.html", {})

def index(response, id):
    ls = Todolist.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n= form.cleaned_data["Name"]
            t= Todolist(name=n)
            t.save()
        return HttpResponseRedirect(f"/{t.id}")
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})