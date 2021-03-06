# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-29 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('county_id', models.IntegerField(primary_key=True, serialize=False)),
                ('county_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubCounty',
            fields=[
                ('subcounty_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subcounty_name', models.CharField(max_length=100)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Counties')),
            ],
        ),
    ]
