from django.urls import path, include
from pims import views

urlpatterns = [
    path('products/', views.ProductView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('products/<int:pk>/stock/', views.ProductStockView.as_view()),
]
