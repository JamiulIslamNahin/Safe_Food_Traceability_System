from django import forms
from .models import Crops, Farm, Storage

class CropForm(forms.ModelForm):
    class Meta:
        model = Crops
        fields = ['Crop_name', 'Crops_type', 'Quantity', 'Plant_Date', 'Harvest_Date']
        widgets = {
            'Plant_Date': forms.DateInput(attrs={'type': 'date'}),
            'Harvest_Date': forms.DateInput(attrs={'type': 'date'}),
        }

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['farm_name', 'farm_address']