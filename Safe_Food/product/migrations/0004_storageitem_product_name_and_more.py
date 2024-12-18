# Generated by Django 5.0.2 on 2024-12-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_storage_humidity_remove_storage_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='storageitem',
            name='product_name',
            field=models.CharField(editable=False, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='storageitem',
            name='product_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='storageitem',
            name='product_type',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
    ]
