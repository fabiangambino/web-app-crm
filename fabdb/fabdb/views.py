from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def advanded_search(request):
    return render(request, 'advanced-search.html')

def contact_view(request):
    return render(request, 'contact-view.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')

def results_list(request):
    return render(request, 'results-list.html')
