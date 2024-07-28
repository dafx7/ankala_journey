from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    USER_ROLES = [
        ('tourist', 'Tourist'),
        ('tourguide', 'Tourguide'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES)

    def __str__(self):
        return self.user.username


class TourGuide(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    experience = models.TextField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    rating = models.FloatField()

    def __str__(self):
        return self.name
