# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email_address = models.EmailField()
    contact_type = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name + " " + self.last_name
