from django.urls import path
from . import views

urlpatterns = [
    path('scaleup', views.home, name='home'),
]