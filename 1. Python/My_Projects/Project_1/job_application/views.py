from django.shortcuts import render
from .froms import ApplicationForm
from .models import Form
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST": # if the user press 'Submit'
        form = ApplicationForm(request.POST) # initialize the class fields
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            
            # populate the db table Form
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)
    
            messages.success(request, "Form submitted successfully!")
        else:
            messages.error(request, "There was an error submitting the form. Check the fields again")
    
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
