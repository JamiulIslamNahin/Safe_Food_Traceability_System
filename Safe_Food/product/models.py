from django.db import models
from dashboard.models import Farm
from authentication.models import UserProfile

# Create your models here.
class Crops(models.Model):
    CROPS_CHOICES = [
        (1, 'Vegetables'),
        (2, 'Fruits'),
        (3, 'Grains'),
        (4, 'Spices')
    ]
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="crops")  
    Crop_name = models.CharField(max_length=50)
    Crops_type = models.IntegerField(choices=CROPS_CHOICES, null=True)
    Quantity = models.FloatField()
    Plant_Date = models.DateField(("Planting Date"), auto_now=False, auto_now_add=False)
    Harvest_Date = models.DateField(("Harvest Date"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.Crop_name
    


class Storage(models.Model):
    storage_name = models.TextField(null=False)
    capacity = models.FloatField(null = False)
    address = models.TextField(null = True)
    owner_name = models.TextField(null=False)
    store_manager = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, null=True, related_name="store_manager"
    )
    temperature = models.FloatField(null= True)
    humidity = models.FloatField(null=True)
    crops = models.ManyToManyField(Crops, related_name="storages", blank= True)
