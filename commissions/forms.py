from django import forms

from .models import Commission, Job, JobApplication

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        exclude=['author']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['commission']
         
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ['job', 'commission', 'applicant', 'status']