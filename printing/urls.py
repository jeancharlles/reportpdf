from django.urls import path
from .views import print_users

urlpatterns = [
    path('printing/', print_users, name='printing'),
]
