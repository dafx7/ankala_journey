from django.contrib import admin
from .models import UserProfile, TourGuide, Rating

admin.site.register(UserProfile)
admin.site.register(TourGuide)
admin.site.register(Rating)
