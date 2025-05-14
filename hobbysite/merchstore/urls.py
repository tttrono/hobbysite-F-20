from django.urls import path

from .views import ProductListView, ProductDetailView, ProductUpdateView, ProductTypeCreateView, ProductCreateView, TransactionListView, CartView 


urlpatterns = [ 
    path('merchstore/items', ProductListView.as_view(), name='items'),
    path('merchstore/item/<int:pk>', ProductDetailView.as_view(), name='item'),
    path('merchstore/item/add', ProductCreateView.as_view(), name='add'),
    path('merchstore/item/<int:pk>/update', ProductUpdateView.as_view(), name='update'),
    path('merchstore/product_type/add', ProductTypeCreateView.as_view(), name='add_product_type'),
    path('merchstore/transactions', TransactionListView.as_view(), name='transactions'),
    path('merchstore/cart', CartView.as_view(), name='cart'),

]

app_name = 'merchstore'