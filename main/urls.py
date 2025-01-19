
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('cart/', views.cart, name='cart'),
    # path('login/', views.login_view, name='login'),
    # path('search/', views.search, name='search'),
]
