from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.http import HttpResponseRedirect
from django.contrib import messages

def home(request):
    return render(request, "index.html")

def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')  
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "create_account.html", {"form": form})