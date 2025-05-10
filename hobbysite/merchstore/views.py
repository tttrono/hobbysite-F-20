from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from . import templates
from .forms import ProductForm, ProductTypeForm
from .models import Product, ProductType

from user_management.models import Profile

class ProductListView(ListView):
    """A list view of products."""
    model = Product
    context_object_name = 'products'
    template_name = "items.html"
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context.update({
            'product_types': ProductType.objects.order_by('name'),
            #'more_context': Model.objects.all(),
        })
        return context
    
class ProductDetailView(DetailView):
    """A detailed view for a product."""
    model = Product
    context_object_name = 'product'
    template_name = "item.html"
    
# class ProductCreateView(LoginRequiredMixin, CreateView):
#     """A view for creating a new product. """
#     model = Product
#     template_name = 'item_add.html'
#     form_class = ProductForm
#
#     def get_success_url(self):
#         return reverse('merchstore:items')
    
@login_required
def create_product(request):
    owner = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = owner
            product.save()
            return redirect('merchstore:items') 
    else:
        form = ProductForm()
        
    return render(request, 'item_add.html', {'form': form})

    
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """A view for updating a product. """
    model = Product
    template_name = 'item_update.html'
    form_class = ProductForm
    
    def get_success_url(self):
        return reverse('merchstore:item', args=[self.object.pk])

# DELETE THIS
class ProductTypeCreateView(LoginRequiredMixin, CreateView):
    """A view for creating new product type. """
    model = ProductType
    template_name = 'add_product_type.html'
    form_class = ProductTypeForm
    
    def get_success_url(self):
        return reverse('merchstore:items')

    