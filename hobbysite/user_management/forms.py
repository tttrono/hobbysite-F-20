from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *

class SignupForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(ModelForm):
    """A form for updating user profile. """
    class Meta:
        model = Profile
        exclude=['user']


