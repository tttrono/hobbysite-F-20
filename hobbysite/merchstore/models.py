from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from enum import unique

from user_management.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin

class ProductType(models.Model):
    """A model for product types or categories."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Product Types'
        ordering = ['name']
        
    def __str__(self):
        return self.name

class Product(models.Model):
    """A model for products in the merchstore."""
    name = models.CharField(max_length=255, unique=True)
    product_type = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL, related_name='product')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='product')
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.PositiveIntegerField()
    
    class Status(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        ON_SALE = 'on sale', 'On Sale'
        OUT_OF_STOCK = 'out of stock', 'Out of Stock'
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.AVAILABLE)
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('merchstore:item', args=[self.pk])
    
class Transaction(LoginRequiredMixin, models.Model):
    buyer = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='transaction')
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name='transaction')
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    
    class Status(models.TextChoices):
        ON_CART = 'on cart', 'On Cart'
        TO_PAY = 'to pay', 'To Pay'
        TO_SHIP = 'to ship', 'To Ship'
        TO_RECEIVE = 'to receive', 'To Receive'
        DELIVERED = 'delivered', 'Delivered'
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ON_CART)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
        
