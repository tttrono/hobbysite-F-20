from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .forms import ProfileUpdateForm
from .models import Profile
  
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """ An update view for user profile. """
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile_update.html'
    
    def get_success_url(self):
        return reverse('home')
    

