from django.shortcuts import render
from django.views.generic import ListView

from .models import Contact


class ContactList(ListView):
    model = Contact
    context_object_name = 'contacts'
    paginate_by = 3