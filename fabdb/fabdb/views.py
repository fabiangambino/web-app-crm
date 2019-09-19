from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, "login.html")

def results(request):
    return render(request, "results.html")

def advanced_search(request):
    return render(request, "advanced-search.html")

def dashboard(request):
    return render(request, "dashboard.html")
