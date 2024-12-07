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
    crops = models.ManyToManyField(Crops, related_name="storages", blank= True)


class StorageItem(models.Model):
    crop = models.ForeignKey(Crops, on_delete=models.CASCADE, related_name="storage_items")
    storage = models.ForeignKey("Storage", on_delete=models.CASCADE, related_name="items")
    date_added = models.DateField(auto_now_add=True)  # Date when added to storage
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    farm_name = models.CharField(max_length=100, editable=False)
    
    # New fields for product information
    product_name = models.CharField(max_length=255, editable=False, null=True)
    product_type = models.CharField(max_length=100, editable=False, null=True)
    product_quantity = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Automatically populate farm_name, product_name, product_type, and product_quantity
        self.farm_name = self.crop.farm.farm_name
        self.product_name = self.crop.Crop_name  # Assuming Crop_name is the product name
        self.product_type = self.crop.Crops_type  # Assuming crop_type is the product type
        self.product_quantity = self.crop.Quantity  # Assuming quantity is available in the Crops model

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_name} in {self.storage.storage_name}"



    def __str__(self):
        return f"{self.crop.Crop_name} in {self.storage.storage_name}"