from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Storage)
admin.site.register(StorageItem)
admin.site.register(Crops)