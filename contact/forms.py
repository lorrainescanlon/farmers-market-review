from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    """
    Form for submitting contact messages
    """

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
