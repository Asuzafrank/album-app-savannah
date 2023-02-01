from .views import UserDetailView
from django.urls import path 
from . import views

urlpatterns = [
    path('show_profile/<int:pk>/', UserDetailView.as_view(), name = 'show_profile'),
    
]