# Generated by Django 5.0.2 on 2024-10-31 17:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('contact_no', models.CharField(max_length=20, null=True)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], null=True)),
                ('nid', models.CharField(max_length=18, null=True)),
                ('dob', models.DateField(null=True)),
                ('address', models.TextField(null=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='profile_picture')),
                ('user_type', models.CharField(choices=[('fm', 'FM'), ('n', 'N'), ('d', 'D'), ('fso', 'FSO')], max_length=3)),
                ('user_identity', models.CharField(editable=False, max_length=10, null=True, unique=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
