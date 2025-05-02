from django import forms
from .models import *

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        exclude=['user']

        
