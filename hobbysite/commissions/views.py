from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.urls.base import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from django.views.generic.list import ListView

from . import templates
from .forms import CommissionForm, JobForm, JobApplicationForm
from .models import Commission, Job, JobApplication

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
            
            profile = Profile.objects.get(user=self.request.user)
            job_applications = JobApplication.objects.filter(applicant=profile)
            jobs_applied = Job.objects.filter(jobapplication__in=job_applications)
           
            context.update({
                'commissions_created': Commission.objects.filter(author=author),
                'commissions_joined': Commission.objects.filter(jobs__in=jobs_applied).distinct(),
                #'job_applications': job_applications,
                #'jobs_applied': jobs_applied,
            })
            
        context.update({
            'open_commissions': Commission.objects.filter(status=Commission.Status.OPEN).order_by('-created_on') ,
            'full_commissions': Commission.objects.filter(status=Commission.Status.FULL).order_by('-created_on'),
            'completed_commissions': Commission.objects.filter(status=Commission.Status.COMPLETED).order_by('-created_on'),
            'discontinued_commissions': Commission.objects.filter(status=Commission.Status.DISCONTINUED).order_by('-created_on'),
        })
        return context

class CommissionDetailView(FormMixin, DetailView):
    """A detail view for commission. """
    model = Commission
    context_object_name = 'commission'
    form_class = JobApplicationForm
    template_name = "commission_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(CommissionDetailView, self).get_context_data(**kwargs)
        commission = Commission.objects.get(pk=self.kwargs.get('pk'))
        
        profile = Profile.objects.get(user=self.request.user)
        job_applications = JobApplication.objects.filter(applicant=profile)
        jobs_applied = Job.objects.filter(jobapplication__in=job_applications)
        
        if self.request.user.is_authenticated:
            logged_user = Profile.objects.get(user=self.request.user)
        else:
            logged_user = None
        
        context.update({
            'logged_user': logged_user,
            'jobs': Job.objects.filter(commission=commission),
            'jobs_applied': jobs_applied,
            'job_applications': job_applications,
        })
        return context
    
    def post(self, request, pk):
        self.object = self.get_object()
        form = self.get_form()
        
        job = Job.objects.get(pk=request.POST.get('job_pk'))
        applicant = Profile.objects.get(user=request.user)
        #commission = Commission.objects.get(pk=self.request.commission.pk)
        
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.job = job
            job_application.applicant = applicant
            
            #job_application.status = Job.Status.PENDING
            job_application.status = JobApplication.Status.ACCEPTED
            
            job.manpower_required = job.manpower_required - 1
            
            if job.manpower_required == 0:
                job.status = Job.Status.FULL
            
            job.save()
            job_application.save()
            
            commission = job_application.job.commission
            
        #     return self.form_valid(form)
        # else:
        #     return self.form_invalid(form)
        return HttpResponseRedirect(reverse('commissions:detail', kwargs={'pk': commission.pk}))
    
    def get_success_url(self):
        return reverse('commissions:detail', args=[self.object.pk])

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
        commission = Commission.objects.get(pk=self.kwargs.get('pk'))
        return reverse('commissions:detail', args=[commission.pk])
    


    
    
    