from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic import TemplateView

from . import templates

class HomePageView(TemplateView):
    template_name = 'home.html'
    
# Alternative using View and render
# from django.views import View
#
# class HomeView(View):
#     def get(self, request):
#         context = {} # Data to pass to the template
#         return render(request, 'home.html', context)