from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """
    Form for submitting market reviews
    """
    
    class Meta:
        model = Review
        fields = ['body', 'stars_rating', 'visit_again']
        labels = {
            'body': 'Your comments',
            'stars_rating': 'Rate your exprience from 0 to 5 stars',
            'visit_again': 'Would you visit again?'
        }
        widgets = {'visit_again': forms.RadioSelect()}
