from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact(request):
    """
    Renders the Contact page
    """
    contact_form = ContactForm()
    context = {
        "contact_form": contact_form, 
    }

    return render( request, "contact/contact.html", context,)