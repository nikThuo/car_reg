# Generated by Django 3.0.6 on 2020-05-30 18:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle_registration', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('transfer_id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('dob', models.DateField()),
                ('pin', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('vehicle_type', models.CharField(max_length=50)),
                ('make', models.CharField(max_length=50)),
                ('vehicle_model', models.CharField(max_length=50)),
                ('year_of_manufacture', models.CharField(max_length=10)),
                ('previous_owner_name', models.CharField(max_length=50)),
                ('previous_owner_mobile', models.IntegerField()),
                ('previous_owner_email', models.EmailField(max_length=30)),
                ('vehicle_status', models.CharField(default='0', max_length=10)),
                ('previous_hash', models.CharField(max_length=100)),
                ('hash', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('national', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_registration.Owner')),
                ('reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_registration.Vehicles')),
            ],
            options={
                'db_table': 'Vehicles_Transfered',
            },
        ),
    ]
