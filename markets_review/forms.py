from .models import Review
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.bootstrap import FormActions


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'stars_rating', 'visit_again']
        labels = {
            'body': 'Your comments',
            'stars_rating': 'Rate your exprience from 0 to 5 stars',
            'visit_again': 'Would you visit again?'
        }
        widgets = {'visit_again': forms.RadioSelect()}