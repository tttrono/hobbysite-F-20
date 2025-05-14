from django.urls import path

from .views import CommissionListView, CommissionDetailView, CommissionCreateView, CommissionUpdateView, JobCreateView

urlpatterns = [ 
    path('commissions/list', CommissionListView.as_view(), name='list'),
    path('commissions/detail/<int:pk>/', CommissionDetailView.as_view(), name='detail'),
    path('commissions/add', CommissionCreateView.as_view(), name='add'),
    path('commissions/<int:pk>/edit', CommissionUpdateView.as_view(), name='edit'),
    
    path('commissions/<int:pk>/job/add', JobCreateView.as_view(), name='job-add'),
]

app_name = 'commissions'