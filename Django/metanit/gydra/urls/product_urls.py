from django.urls import path
from api.views import ProductListView, ProductDetailView, ProductCreateView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
