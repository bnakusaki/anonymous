from django.urls import path
from . import views

urlpatterns = [
    path('demoPage/', views.demoPage)
]
