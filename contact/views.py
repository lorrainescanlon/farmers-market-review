from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


# Create your views here.
def contact(request):
    """
    Renders the Contact page and form
    """

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Contact form "
                "recieved! We appreciate your feedback & will be in contact"
                " shortly.")

    contact_form = ContactForm()
    context = {
        "contact_form": contact_form,
    }

    return render(request, "contact/contact.html", context,)
