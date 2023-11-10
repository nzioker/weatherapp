from django.conf import settings
from django import forms


class SearchForm(forms.Form):
    search_bar = forms.CharField(label="Search", max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Type in a City'}))
    
    
    