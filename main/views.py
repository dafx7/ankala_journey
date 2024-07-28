from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import UserProfile
# Create your views here.


def index(request):
    return render(request, "main/index.html")


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
