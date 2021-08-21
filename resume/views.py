from django.shortcuts import render
from resume.forms import LetterForm
from resume.models import Letter
from django.http import HttpResponse
from datetime import datetime



# Create your views here.
def Home(request):
    return render(request,template_name='about.html')

def Contact(request):
    
    if request.method == "GET":
        form = LetterForm()

    if request.method == "POST":
        form = LetterForm(request.POST)

        if form.is_valid():
            print("data", form.cleaned_data)
            Letter.objects.create(**form.cleaned_data)
        else:
            print("Form is not valid")
            form = LetterForm()

    return render(request,template_name='contact.html')

def Resume(request):
    return render(request,template_name='resume.html')
