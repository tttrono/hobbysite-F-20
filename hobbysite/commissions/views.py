from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from . import templates
from .forms import CommissionForm
from .models import Commission, Comment
from django.urls.base import reverse_lazy

class CommissionListView(ListView):
    """A view for commissions as list."""
    model = Commission
    context_object_name = 'commissions'
    template_name = "commissions_list.html"
                    
def detail(request, pk):
    """A view for a detailed view of a commission with comments."""
    commission = Commission.objects.get(pk=pk)
    comments = Comment.objects.filter(commission__pk=pk)
    context = {
        'commission' : commission,
        'comments': comments
    }
            
    return render(request, "commission_detail.html", context)

class CommissionCreateView(CreateView):
    model = Commission
    template_name = 'commission_add.html'
    form_class = CommissionForm
    
    def get_success_url(self):
        return reverse('commissions:list')
    
class CommissionUpdateView(UpdateView):
    model = Commission
    template_name = 'commission_edit.html'
    form_class = CommissionForm
    
    def get_success_url(self):
        return reverse('commissions:detail', args=[self.object.pk])
    
    