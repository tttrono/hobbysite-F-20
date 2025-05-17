from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='update'),
]

app_name = 'user_management'

