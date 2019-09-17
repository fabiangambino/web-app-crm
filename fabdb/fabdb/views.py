from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def advanded_search(request):
    return render(request, 'advanced-search.html')

def results_list(request):
    return render(request, 'results-list.html')
