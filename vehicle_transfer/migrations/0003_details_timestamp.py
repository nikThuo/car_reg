# Generated by Django 3.0.6 on 2020-05-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_transfer', '0002_details_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
