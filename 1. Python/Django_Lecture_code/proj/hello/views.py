from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def marto(request):
    return HttpResponse("<h1 style='color:blue'> Hello Marto </h1>") # responds with html: Hello Marto

def david(request):
    return HttpResponse("Hello David")

def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()}) # we can use name in the html as a variable

# def greet(request, name):
#    return HttpResponse(f"Hello {name.capitalize()}")