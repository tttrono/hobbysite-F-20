from django import forms

from .models import Product, ProductType, Transaction

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner']
        #fields="__all__"

        # def save(self, commit=True):
        #     instance = super().save(commit=False)
        #     instance.owner = Profile.objects.get(user=self.request.user)  
        #     if commit:
        #         instance.save()
        #     return instance

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model=Product
#         fields="__all__"
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['Owner'].disabled=True

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = '__all__'
        
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        #exclude = ['buyer']
        exclude = ['buyer', 'product']
        

        