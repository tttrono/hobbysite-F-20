from django.urls import path

from .views import CommissionListView, CommissionDetailView


urlpatterns = [ 
    path('commissions/list', CommissionListView.as_view(), name='list'),
    path('commissions/detail/<int:pk>', CommissionDetailView.as_view(), name='detail'),
]

app_name = 'commissions'