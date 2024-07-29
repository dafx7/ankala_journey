import os
import django

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ankala_website.settings')
django.setup()

from main.models import TourGuide

# Data sample dengan nama
tour_guides_data = [
    {'name': 'Alice Smith', 'age': 25, 'gender': 'F', 'experience': 'Experienced in hiking', 'location': 'Medan, North Sumatra', 'status': 'active'},
    {'name': 'Maria Garcia', 'age': 30, 'gender': 'F', 'experience': 'Experienced in city tours', 'location': 'Medan, North Sumatra', 'status': 'active'},
    {'name': 'Sophia Johnson', 'age': 27, 'gender': 'F', 'experience': 'Experienced in cultural tours', 'location': 'Medan, North Sumatra', 'status': 'active'},
    {'name': 'Emily Brown', 'age': 35, 'gender': 'F', 'experience': 'Experienced in historical tours', 'location': 'Medan, North Sumatra', 'status': 'active'},
    {'name': 'Olivia Jones', 'age': 29, 'gender': 'F', 'experience': 'Experienced in culinary tours', 'location': 'Medan, North Sumatra', 'status': 'active'},
    {'name': 'Ava Miller', 'age': 33, 'gender': 'F', 'experience': 'Experienced in adventure tours', 'location': 'Medan, North Sumatra', 'status': 'active'},
    {'name': 'Isabella Wilson', 'age': 24, 'gender': 'F', 'experience': 'Experienced in nature tours', 'location': 'Medan, North Sumatra', 'status': 'active'},
    {'name': 'Mia Moore', 'age': 31, 'gender': 'F', 'experience': 'Experienced in eco tours', 'location': 'Medan, North Sumatra', 'status': 'active'},
    {'name': 'Amelia Taylor', 'age': 28, 'gender': 'F', 'experience': 'Experienced in night tours', 'location': 'Medan, North Sumatra', 'status': 'active'},
    {'name': 'Harper Anderson', 'age': 26, 'gender': 'F', 'experience': 'Experienced in family tours', 'location': 'Medan, North Sumatra', 'status': 'active'}
]

# Tambahkan data sample ke database
for guide_data in tour_guides_data:
    TourGuide.objects.create(**guide_data)

print("Sample data added successfully!")
