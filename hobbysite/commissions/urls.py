from django.urls import path

from .views import CommissionListView, CommissionDetailView, CommissionCreateView, CommissionUpdateView, create_job #JobCreateView

urlpatterns = [ 
    path('commissions/list', CommissionListView.as_view(), name='list'),
    path('commissions/detail/<int:pk>/', CommissionDetailView.as_view(), name='detail'),
    path('commissions/add', CommissionCreateView.as_view(), name='add'),
    path('commissions/<int:pk>/edit', CommissionUpdateView.as_view(), name='edit'),
    
    path('commissions/<int:pk>/job/add', create_job, name='job-add'),
]

app_name = 'commissions'