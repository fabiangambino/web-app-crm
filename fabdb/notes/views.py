from django.http import HttpResponse
from django.shortcuts import render

def notes(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'notes/all-notes.html')
