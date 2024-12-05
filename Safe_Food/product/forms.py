from django import forms
from .models import *

class CropsForm(forms.ModelForm):
    class Meta:
        model = Crops
        fields = ['Crop_name', 'Crops_type', 'Quantity', 'Plant_Date', 'Harvest_Date']