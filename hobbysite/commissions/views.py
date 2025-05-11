from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from . import templates
from .forms import CommissionForm, JobForm
from .models import Commission, Job
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
    
    def get_context_data(self, **kwargs):
        context = super(CommissionDetailView, self).get_context_data(**kwargs)
        commission = Commission.objects.get(pk=self.kwargs.get('pk'))
        
        context.update({
            'jobs': Job.objects.filter(commission=commission),
            #'more_context': Model.objects.all(),
        })
        return context

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
    
# class JobCreateView(CreateView):
#     """A view for creating a job. """
#     model = Job
#     template_name = 'job_add.html'
#     form_class = JobForm
#
#     def get_success_url(self):
#         return reverse('commissions:detail', args=[self.object.pk])
    
@login_required
def create_job(request, pk):
    """ A function-based view to create a job. """
    commission = Commission.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.commission = commission
            job.save()
            return redirect('commissions:detail', args=[self.object.commission.pk])
    else:
        form = JobForm()
        
    return render(request, 'job_add.html', {'form': form})
    
    
    