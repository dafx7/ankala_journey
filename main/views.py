from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, RatingForm
from .models import UserProfile, TourGuide, Rating
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    tour_guides = TourGuide.objects.filter(status='active').order_by('-rating')[:10]
    # Mendapatkan 10 tourguide dengan rating tertinggi yang memiliki gender female
    female_tourguides = TourGuide.objects.filter(status='active', gender='F').order_by('-rating')[:10]

    # Mendapatkan 10 tourguide dengan rating tertinggi yang memiliki lokasi 'Samosir, North Sumatra'
    samosir_tourguides = TourGuide.objects.filter(status='active', location='Samosir, North Sumatra').order_by(
        '-rating')[:10]
    return render(request, "main/index.html", {
                'tourguides': tour_guides,
                'female_tourguides': female_tourguides,
                'samosir_tourguides': samosir_tourguides
                })


@login_required
def tour_guide_cv(request, id):
    tourguide = get_object_or_404(TourGuide, pk=id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.tourguide = tourguide
            rating.user = request.user
            rating.save()
            tourguide.update_rating(rating.rating)
            return redirect('cv', id=tourguide.id)
    else:
        form = RatingForm()
    return render(request, 'main/cv.html', {'tourguide': tourguide, 'form': form})


def payment(request):
    return render(request, 'main/payment.html')


def tour_guide_reviews(request, id):
    tourguide = get_object_or_404(TourGuide, pk=id)
    reviews = Rating.objects.filter(tourguide=tourguide)
    return render(request, 'main/review.html', {'tourguide': tourguide, 'reviews': reviews})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            UserProfile.objects.create(user=user, role=role)
            login(request, user)
            return redirect('index')
        else:
            # Print form errors to debug
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def privacy_policy(request):
    return render(request, 'main/pp.html')


def terms_condition(request):
    return render(request, 'main/tac.html')


def faq(request):
    return render(request, 'main/faq.html')


def about_us(request):
    return render(request, 'main/about-us.html')
