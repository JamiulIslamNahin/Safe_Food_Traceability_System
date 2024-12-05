from django.db import models
from django.utils.translation import gettext_lazy as _
from authentication.models import UserProfile


class Farm(models.Model):
    farm_name = models.CharField(max_length=50)
    farm_address = models.TextField(null=True)
    farm_manager = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, related_name="farm_manager")
    
