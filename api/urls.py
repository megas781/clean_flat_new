from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('orders', views.OrderView.as_view(), name='api-order-url'),
    path('articles/<int:pk>', views.OrderView.as_view())
]
