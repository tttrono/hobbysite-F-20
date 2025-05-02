from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='update'),
    
    #path('create/', ProfileCreateView.as_view(), name='profile:create'),
    #path('profile/<int:pk>/', ProfileDetailView.as_view(), name='detail'),
    #path('profile/<int:pk>/update', ProfileUpdateView.as_view(), name='update'),
    #path('profile/', profileUpdateView, name='update'),
]

app_name = 'user_management'

