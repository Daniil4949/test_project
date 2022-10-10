from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """Form for searching posts"""
    title = forms.CharField(label='Your feedback', widget=forms.TextInput(attrs={'class': 'form-input'})),

    class Meta:
        model = Feedback
        fields = ('text',)

