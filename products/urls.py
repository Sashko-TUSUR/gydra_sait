from django.urls import path
from . import views

urlpatterns = [
    # Routes for working with products
    path('add_product/', views.add_product, name='add_product'),
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/edit/', views.edit_product, name='edit_product'),

    # Routes for working with type products
    path('add_type/', views.add_type_product, name='add_type_product'),
    path('type_products/', views.type_product_list, name='type_product_list'),
    path('type_product/<int:type_id>/', views.type_product_detail, name='type_product_detail'),
    path('type_product/<int:type_id>/edit/', views.edit_type_product, name='edit_type_product'),
]