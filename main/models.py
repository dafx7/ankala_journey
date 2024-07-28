from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


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
    rating = models.FloatField(default=0.0)
    total_ratings = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    num_raters = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def update_rating(self, new_rating):
        self.total_ratings += Decimal(new_rating)
        self.num_raters += 1
        self.rating = float(self.total_ratings / self.num_raters)
        self.save()


class Rating(models.Model):
    tourguide = models.ForeignKey(TourGuide, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', default=1)  # Default user ID
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
