from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .forms import SignupForm, ProfileUpdateForm
from .models import Profile

# class ProfileDetailView(DetailView):
#     model = Profile
#     template_name = 'profile_detail.html'
  
class ProfileUpdateView(UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'profile_update.html'
    
    def get_success_url(self):
        return reverse('home')
    
# def profileUpdateView(request, object_id):
#     try:
#         obj = Profile.objects.get(pk=object_id)
#         object_exists = True
#     except Profile.DoesNotExist:
#         object_exists = False

# def profileUpdateView(request, pk):
#     #obj = get_object_or_404(Profile, pk = request.user.pk)
#     obj = Profile.objects.get(pk=pk)
#     form = ProfileUpdateForm(request.POST or None, instance = obj)
#
#     if form.is_valid():
#         form.save()
#         return reverse('home')
#
#     #context["form"] = form
#
#     context = {
#         'form' : form,
#     }
#
#     return render(request, "profile_update.html", context)