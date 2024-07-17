from django.db import models
from Accounts.models import User

class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=15,null=False, unique=True, db_index=True)

class ContactDetail(models.Model):
    full_name = models.CharField(max_length=128)
    address = models.TextField()
    description = models.TextField()

class Phone2ContactDetail(models.Model):
    phone_id = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE)    
    detail_id = models.ForeignKey(ContactDetail, on_delete=models.CASCADE)

class UserContactsDetail(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)    
    phone_detail_id = models.ForeignKey(Phone2ContactDetail, on_delete=models.CASCADE)