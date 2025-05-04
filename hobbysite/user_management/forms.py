from django.forms import ModelForm

from .models import *

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        exclude=['user']


