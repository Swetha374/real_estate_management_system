from django import forms
from .models import Property,Unit

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'location', 'features']


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['unit_type', 'rent_cost']