from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from core.views import custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]

handler404 = custom_404_view
handler500 = 'core.views.error_500'

if settings.DEBUG:
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

