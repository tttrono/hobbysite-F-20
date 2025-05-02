from django.shortcuts import render
from django.urls import reverse

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .forms import ProfileUpdateForm
from .models import Profile

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile_detail.html'
  
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile_update.html'
    
    def get_success_url(self):
        return reverse('home')
    