from django.urls import path

from .views import CommissionListView, detail

urlpatterns = [ 
    path('commissions/list', CommissionListView.as_view(), name='list'),
    path('commissions/detail/<int:id>/', detail, name='detail'),
]

app_name = 'commissions'