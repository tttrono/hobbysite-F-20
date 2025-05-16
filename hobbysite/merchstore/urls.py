from django.urls import path

from .views import ProductListView, ProductDetailView, ProductUpdateView, ProductTypeCreateView, ProductCreateView, TransactionListView, CartView 


urlpatterns = [ 
    path('items', ProductListView.as_view(), name='items'),
    path('item/<int:pk>', ProductDetailView.as_view(), name='item'),
    path('item/add', ProductCreateView.as_view(), name='add'),
    path('item/<int:pk>/update', ProductUpdateView.as_view(), name='update'),
    path('product_type/add', ProductTypeCreateView.as_view(), name='add_product_type'),
    path('transactions', TransactionListView.as_view(), name='transactions'),
    path('cart', CartView.as_view(), name='cart'),

]

app_name = 'merchstore'