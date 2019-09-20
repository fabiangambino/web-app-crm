from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact

def all_contacts(request):
    contacts = Contact.objects.all().order_by('date_created')
    return render(request, 'contacts/all-contacts.html', {'contacts': contacts})

def contact_view(request):
    return render(request, 'contacts/contact-view.html')
