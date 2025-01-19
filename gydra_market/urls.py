from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = ([
                   path('admin/', admin.site.urls),
                   path('', include('main.urls')),
                   path('products/', include('products.urls')),
                   path('admin/', admin.site.urls),
                   path('accounts/', include('accounts.urls')),  # Ваши маршруты для регистрации и входа
                   path('accounts/', include('django.contrib.auth.urls')),
                   path('', RedirectView.as_view(url='/accounts/login/', permanent=False), name='home'),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
               static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
