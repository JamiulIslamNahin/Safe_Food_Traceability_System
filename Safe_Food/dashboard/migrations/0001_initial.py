# Generated by Django 5.0.2 on 2024-12-06 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_name', models.CharField(max_length=50)),
                ('farm_address', models.TextField(null=True)),
                ('farm_manager', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='farm_manager', to='authentication.userprofile')),
            ],
        ),
    ]