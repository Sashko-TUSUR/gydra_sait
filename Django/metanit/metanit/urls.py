from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('api.auth_urls')),       # Аутентификация
    path('api/products/', include('api.products_urls')),  # Товары
    path('api/cart/', include('api.cart_urls')),       # Корзина
    path('api/orders/', include('api.orders_urls')),   # Заказы
    path('api/reviews/', include('api.reviews_urls')) # Отзывы
]