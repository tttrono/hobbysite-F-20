from django.forms import ModelForm

from .models import *

class ProfileUpdateForm(ModelForm):
    """A form for updating user profile. """
    class Meta:
        model = Profile
        exclude=['user']


