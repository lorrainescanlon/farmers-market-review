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
    if request.method =="POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Contact form recieved! We appreciate your feedback & will be in contact shortly.")

    contact_form = ContactForm()
    context = {
        "contact_form": contact_form, 
    }

    return render( request, "contact/contact.html", context,)