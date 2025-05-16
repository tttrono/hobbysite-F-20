from django.urls import path

from .views import CommissionListView, CommissionDetailView, CommissionCreateView, CommissionUpdateView, JobCreateView

urlpatterns = [ 
    path('list', CommissionListView.as_view(), name='list'),
    path('detail/<int:pk>/', CommissionDetailView.as_view(), name='detail'),
    path('add', CommissionCreateView.as_view(), name='add'),
    path('<int:pk>/edit', CommissionUpdateView.as_view(), name='edit'),
    
    path('<int:pk>/job/add', JobCreateView.as_view(), name='job-add'),
]

app_name = 'commissions'