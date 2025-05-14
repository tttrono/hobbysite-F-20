from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.urls.base import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from . import templates
from .forms import CommissionForm, JobForm
from .models import Commission, Job

from user_management.models import Profile

class CommissionListView(ListView):
    """A view for commissions as list."""
    model = Commission
    context_object_name = 'commissions'
    template_name = "commissions_list.html"
    
    def get_context_data(self, **kwargs):
        context = super(CommissionListView, self).get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            author = Profile.objects.get(user=self.request.user)
        else:
            author = None
        
        context.update({
            'commissions_created': Commission.objects.filter(author=author),
            
            'open_commissions': Commission.objects.filter(status=Commission.Status.OPEN),
            'full_commissions': Commission.objects.filter(status=Commission.Status.FULL),
            'completed_commissions': Commission.objects.filter(status=Commission.Status.COMPLETED),
            'discontinued_commissions': Commission.objects.filter(status=Commission.Status.DISCONTINUED),
        })
        return context

class CommissionDetailView(DetailView):
    """A detail view for commission. """
    model = Commission
    context_object_name = 'commission'
    template_name = "commission_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(CommissionDetailView, self).get_context_data(**kwargs)
        commission = Commission.objects.get(pk=self.kwargs.get('pk'))
        
        context.update({
            'jobs': Job.objects.filter(commission=commission),
        })
        return context

class CommissionCreateView(LoginRequiredMixin, CreateView):
    """A view for creating a new commission. """
    model = Commission
    template_name = 'commission_add.html'
    form_class = CommissionForm
    
    def form_valid(self, form):
        form.instance.author = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('commissions:list')
    
class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    """A view for updating a commission. """
    model = Commission
    template_name = 'commission_edit.html'
    form_class = CommissionForm
    
    def get_success_url(self):
        return reverse('commissions:detail', args=[self.object.pk])
    
class JobCreateView(LoginRequiredMixin, CreateView):
    """A view for creating a job. """
    model = Job
    template_name = 'job_add.html'
    form_class = JobForm

    def form_valid(self, form):
        form.instance.commission = Commission.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('commissions:detail', args=[self.object.pk])
    


    
    
    