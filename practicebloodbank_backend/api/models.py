from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    medical_history = models.TextField(blank=True)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    
    BLOOD_TYPES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-')
    ]
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES, null=True, blank=True)


class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField()

class BloodInventory(models.Model):
    BLOOD_TYPES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-')
    ]
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_donated = models.DateField(auto_now_add=True)