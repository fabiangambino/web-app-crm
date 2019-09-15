# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . models import Contact

# Create your views here.
def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/all-contacts.html',{'contacts':contacts})

def contact_view(request):
    return render(request, 'contacts/contact-view.html')
