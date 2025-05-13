from django import forms

from .models import Commission, Job

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        exclude=['author']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['commission']