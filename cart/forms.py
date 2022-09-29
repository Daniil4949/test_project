from django import forms
from books.models import Book
from .models import Payment


class SearchBookForm(forms.ModelForm):
    """Form for searching posts"""
    title = forms.CharField(label='title', widget=forms.TextInput(attrs={'class': 'form-input'})),

    class Meta:
        model = Book
        fields = ('title',)


class PaymentForm(forms.ModelForm):
    number_of_card = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    validity_period = forms.CharField(label='xx/xx', widget=forms.TextInput(attrs={'class': 'form-input'}))
    cvv = forms.CharField()

    class Meta:
        model = Payment
        fields = ('number_of_card', 'validity_period', 'cvv', )
        widgets = {
            'number_of_card': forms.TextInput(attrs={'class': 'form-input'}),
            'validity_period': forms.TextInput(attrs={'class': 'form-input'}),
            'cvv': forms.TextInput(attrs={'class': 'form-input'}),
        }