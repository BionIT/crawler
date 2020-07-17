from django import forms

class SearchInputForm(forms.Form):
    source = forms.CharField()