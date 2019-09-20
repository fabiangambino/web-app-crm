from django.http import HttpResponse
from django.shortcuts import render

def notes(request):
    return render(request, 'notes/all-notes.html')
