from django.http import HttpResponse
from django.shortcuts import render

def all_contacts(request):
    return render(request, 'contacts/all-contacts.html')

def contact_view(request):
    return render(request, 'contacts/contact-view.html')
