from django.db import models
from django.urls import reverse
from enum import unique

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
    """A model for products in the merch store."""
    name = models.CharField(max_length=255, unique=True)
    productType = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL, related_name='product')
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('merchstore:item', args=[self.pk])
        
