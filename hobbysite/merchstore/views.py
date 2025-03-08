from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from . import templates
from .models import Product, ProductType

class ProductListView(ListView):
    """A view for product items as list."""
    model = Product
    context_object_name = 'products'
    template_name = "items.html"
    
class ProductDetailView(DetailView):
    """A view for detailed view of a product."""
    model = Product
    context_object_name = 'product'
    template_name = "item.html"
    