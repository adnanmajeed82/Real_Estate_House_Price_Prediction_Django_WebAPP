# prediction/forms.py
from django import forms
from .models import House

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['area', 'bedrooms', 'bathrooms']
