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
    validity_period_month = forms.CharField(label='email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    validity_period_year = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Payment
        fields = ('number_of_card', 'validity_period_month', 'validity_period_year', )
        widgets = {
            'number_of_card': forms.TextInput(attrs={'class': 'form-input'}),
            'validity_period_month': forms.TextInput(attrs={'class': 'form-input'}),
            'validity_period_year': forms.TextInput(attrs={'class': 'form-input'}),

        }