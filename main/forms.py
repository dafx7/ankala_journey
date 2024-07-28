from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    role = forms.ChoiceField(choices=UserProfile.USER_ROLES, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')
