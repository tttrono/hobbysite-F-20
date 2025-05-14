from django import template
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from django.views.generic.list import ListView

from . import templates
from .forms import ProductForm, ProductTypeForm, TransactionForm
from .models import Product, ProductType, Transaction

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
        logged_user = Profile.objects.get(user=self.request.user)
        
        context.update({
            'logged_user': logged_user,
        })
        return context

    def post(self, request, *args, **kwargs):
        buyer = Profile.objects.get(user=request.user)
        product = Product.objects.get(pk=self.kwargs.get('pk'))
        self.object = self.get_object()
        form = self.get_form()
        
        ctx = self.get_context_data(**kwargs)
        ctx["errors"] = {}
        
        # amount = form.PositiveIntegerField(validators=[MaxValueValidator(product.stock)],
        # help_text="Only %s stock/s left" % (product.stock))
        
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.buyer = buyer
            transaction.product = product
            
            if product.stock < transaction.amount:
                ctx["errors"]["overbuy"] = True
                return render(request, self.template_name, context=ctx)
            
            product.stock = product.stock - transaction.amount
            transaction.status = Transaction.Status.ON_CART
            
            if product.stock == 0:
                product.status = Product.Status.OUT_OF_STOCK
            
            product.save()
            
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        product = Product.objects.get(pk=self.kwargs.get('pk'))
        
        if amount > product.stock:
            raise ValueError("Quantity greater than stock.")
        return amount
    
    def form_valid(self, form):
        form.save()
        return redirect(reverse('merchstore:cart'))

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
    
class CartView(LoginRequiredMixin, ListView):
    """A view listing all buyer transactions of the logged-in user. """
    model = Transaction
    context_object_name = 'transactions'
    template_name = 'cart.html'
    
    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)     
        
        buyer = Profile.objects.get(user=self.request.user)
        buyer_transactions = Transaction.objects.filter(buyer=buyer)
        #sellers_all = Profile.objects.all()
        
        context.update({
            'buyer_transactions': buyer_transactions.order_by('product__owner'),
            #'sellers_all': sellers_all, 
        })
        return context
    
class TransactionListView(LoginRequiredMixin, ListView):
    """A view listing all seller transactions of the logged-in user. """
    model = Transaction
    context_object_name = 'transactions'
    template_name = 'transactions.html'
    
    def get_context_data(self, **kwargs):
        context = super(TransactionListView, self).get_context_data(**kwargs)     
        
        seller = Profile.objects.get(user=self.request.user)
        seller_items = Product.objects.filter(owner=seller)
        seller_transactions = Transaction.objects.filter(product__in=seller_items)
        buyers_all = Profile.objects.all()
        
        context.update({
            'seller_transactions': seller_transactions.order_by('buyer'),
            'buyers_all': buyers_all, 
        })
        return context
    