from django import forms

from .models import Commission, Job

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['commission']