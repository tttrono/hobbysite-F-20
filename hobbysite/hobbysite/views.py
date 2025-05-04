from django.shortcuts import render
from django.http import HttpResponse

from . import templates

def home(request):
    return render(request, "home.html", context=None)
user_management
