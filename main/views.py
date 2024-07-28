from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import UserProfile, TourGuide
# Create your views here.


def index(request):
    tour_guides = TourGuide.objects.filter(status='active').order_by('-rating')[:10]
    return render(request, "main/index.html", {'tourguides': tour_guides})


def tour_guide_cv(request, id):
    tour_guide = get_object_or_404(TourGuide, pk=id)
    return render(request, 'main/cv.html', {'tourguide': tour_guide})


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
