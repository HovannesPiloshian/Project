from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:category_id>/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Add this line
]
