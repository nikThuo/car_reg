from django.db import models

# Create your models here.
from general.models import Counties, SubCounty
import uuid


class Users(models.Model):
    transaction_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    mobile = models.IntegerField(null=True)
    email = models.EmailField(max_length=50, null=True)
    pin = models.CharField(max_length=50, null=True)
    national_id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=300)
    status = models.CharField(max_length=20, default='active')
    user_type = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'Users'



