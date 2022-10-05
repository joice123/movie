from django import forms
from .models import Movie
from django.forms import ModelForm


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'desc', 'img', 'year']
