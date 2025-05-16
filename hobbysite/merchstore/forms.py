from django import forms
from django.core.validators import MaxValueValidator

from .models import Product, ProductType, Transaction


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner']

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = '__all__'
        
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['buyer', 'product', 'status']
        
        def __init__(self, *args, **kwargs):
            product = self.request.product
            self.fields['amount'].validators.append(MaxValueValidator(product.stock, "Quantity greater than stock."))



        
                
        

        