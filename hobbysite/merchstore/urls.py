from django.urls import path

from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductTypeCreateView


urlpatterns = [ 
    path('merchstore/items', ProductListView.as_view(), name='items'),
    path('merchstore/item/<int:pk>', ProductDetailView.as_view(), name='item'),
    path('merchstore/item/add', ProductCreateView.as_view(), name='add'),
    path('merchstore/item/<int:pk>/update', ProductUpdateView.as_view(), name='update'),
    path('merchstore/product_type/add', ProductTypeCreateView.as_view(), name='add_product_type')
]

app_name = 'merchstore'