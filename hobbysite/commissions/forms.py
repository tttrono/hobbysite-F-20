from django import forms

from .models import Commission, Comment

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'