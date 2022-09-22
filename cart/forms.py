from django import forms
from books.models import Book


class SearchBookForm(forms.ModelForm):
    """Form for searching posts"""
    title = forms.CharField(label='title', widget=forms.TextInput(attrs={'class': 'form-input'})),

    class Meta:
        model = Book
        fields = ('title',)