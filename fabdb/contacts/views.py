from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contact

def all_contacts(request):
    contacts = Contact.objects.all().order_by('date_created')
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'contacts/all-contacts.html', {'contacts': contacts})

def contact_view(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'contacts/contact-view.html')
