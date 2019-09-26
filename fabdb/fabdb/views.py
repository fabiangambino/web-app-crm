from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            return redirect('/dashboard')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form':form})

def results(request):
    return render(request, "results.html")

def advanced_search(request):
    return render(request, "advanced-search.html")

def dashboard(request):
    return render(request, "dashboard.html")
