from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from . import templates
from .forms import ProductForm, ProductTypeForm
from .models import Product, ProductType

class ProductListView(ListView):
    """A detailed view of products."""
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
    
class ProductCreateView(CreateView):
    """A view for creating a new product. """
    model = Product
    template_name = 'item_add.html'
    form_class = ProductForm
    
    def get_success_url(self):
        return reverse('merchstore:items')
    
class ProductUpdateView(UpdateView):
    """A view for updating a product. """
    model = Product
    template_name = 'item_update.html'
    form_class = ProductForm
    
    def get_success_url(self):
        return reverse('merchstore:item', args=[self.object.pk])
    
class ProductTypeCreateView(CreateView):
    model = ProductType
    template_name = 'add_product_type.html'
    form_class = ProductTypeForm
    
    def get_success_url(self):
        return reverse('merchstore:items')

    