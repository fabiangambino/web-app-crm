from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            return redirect('/dashboard')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')

def results(request):
    return render(request, "results.html")

def advanced_search(request):
    return render(request, "advanced-search.html")

def dashboard(request):
    return render(request, "dashboard.html")
