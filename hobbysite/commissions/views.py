from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from . import templates
from .models import Commission, Comment

class CommissionListView(ListView):
    """A view for commissions as list."""
    model = Commission
    context_object_name = 'commissions'
    template_name = "list.html"
    
class CommissionDetailView(DetailView):
    """A view for a detailed view of a commission with comments."""
    model = Commission
    context_object_name = 'commission'
    template_name = "detail.html"
    
