from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from django.views.generic.list import ListView

from . import templates
from .forms import ProductForm, ProductTypeForm, TransactionForm
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
    
class ProductDetailView(LoginRequiredMixin, FormMixin, DetailView):
    """A detailed view for a product."""
    model = Product
    form_class = TransactionForm
    context_object_name = 'product'
    template_name = "item.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        buyer = Profile.objects.get(user=request.user)
        product = Product.objects.get(pk=self.kwargs.get('pk'))
        
        self.object = self.get_object()
        form = self.get_form()
       
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.buyer = buyer
            transaction.product = product
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect(reverse('merchstore:item', kwargs={'pk': self.object.pk}))
        # REDIRECT TO CARTVIEW

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    """A view for creating a new product. """
    model = Product
    template_name = 'item_add.html'
    form_class = ProductForm

    def form_valid(self, form):
        form.instance.owner = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('merchstore:items')

    
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

    