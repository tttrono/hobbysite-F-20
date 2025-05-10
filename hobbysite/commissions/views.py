from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from . import templates
from .forms import CommissionForm
from .models import Commission
from django.urls.base import reverse_lazy

class CommissionListView(ListView):
    """A view for commissions as list."""
    model = Commission
    context_object_name = 'commissions'
    template_name = "commissions_list.html"

class CommissionDetailView(DetailView):
    """A detail view for commission. """
    model = Commission
    context_object_name = 'commission'
    template_name = "commission_detail.html"

class CommissionCreateView(LoginRequiredMixin, CreateView):
    """A view for creating a new commission. """
    model = Commission
    template_name = 'commission_add.html'
    form_class = CommissionForm
    
    def get_success_url(self):
        return reverse('commissions:list')
    
class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    """A view for updating a commission. """
    model = Commission
    template_name = 'commission_edit.html'
    form_class = CommissionForm
    
    def get_success_url(self):
        return reverse('commissions:detail', args=[self.object.pk])
    
    