from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', ProfileUpdateView.as_view(), name='update'),
]

app_name = 'user_management'

