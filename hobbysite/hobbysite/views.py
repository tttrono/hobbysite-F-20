from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User

from . import templates
from .forms import SignupForm

def home(request):
    return render(request, "home.html", context=None)

class SignupView(CreateView):
    """A signup view for a new user. """
    model = User
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        """ auto-login once signed up. """
        user = form.save()
        login(self.request, user) 
        return redirect(self.success_url)
    
    