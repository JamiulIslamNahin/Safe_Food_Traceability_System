from django import forms
from .models import *
from django.forms import Form, ModelChoiceField, CharField, FloatField, Textarea

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


class AddToStorageForm(forms.ModelForm):
    temperature = forms.FloatField(required=True, label="Storage Temperature")
    humidity = forms.FloatField(required=True, label="Storage Humidity")

    class Meta:
        model = StorageItem
        fields = ["temperature", "humidity"]  # Expose only these fields to the form


class AssignStorageForm(Form):
    storage = ModelChoiceField(
        queryset=Storage.objects.filter(store_manager__isnull=True),
        label="Available Storages",
        required=False,
    )

class AddStorageForm(Form):
    storage_name = CharField(max_length=100, label="Storage Name")
    capacity = FloatField(label="Capacity")
    address = CharField(widget=Textarea, label="Address")
    owner_name = CharField(max_length=100, label="Owner Name")