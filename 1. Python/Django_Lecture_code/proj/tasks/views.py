from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def index(request):
    # This line checks if the key "tasks" is not already present in the current request.session dictionary.
    # Essentially, it checks whether there is already a session variable named "tasks".
    if "tasks" not in request.session:
        request.session["tasks"] = [] # If the key "tasks" is not found in the session, this line initializes it by setting to an empty list
    return render(request, "tasks/index.html", {"tasks": request.session["tasks"]}) # html template will have access to request.session["tasks"] variable by the key "tasks"

def add(request):
    if request.method == "POST": 
        form = NewTaskForm(request.POST) # request.POST contains the user data entered in the form
        if form.is_valid():
            task = form.cleaned_data['task']
            #priority = form.cleaned_data['priority']
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index")) # loads the index page (a.k.a calls the index())
        else:
            return render(request, "tasks/add.html", {"form": form}) # displays errors

    return render(request, "tasks/add.html", {"form": NewTaskForm()})