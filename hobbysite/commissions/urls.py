from django.urls import path

from .views import CommissionListView, detail, CommissionCreateView, CommissionUpdateView

urlpatterns = [ 
    path('commissions/list', CommissionListView.as_view(), name='list'),
    path('commissions/detail/<int:pk>/', detail, name='detail'),
    path('commissions/add', CommissionCreateView.as_view(), name='add'),
    path('commissions/<int:pk>/edit', CommissionUpdateView.as_view(), name='edit'),
]

app_name = 'commissions'