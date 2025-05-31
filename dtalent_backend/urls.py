"""
Configuración de URLs para el proyecto dtalent_backend.
"""
#importar librerías correspondientes
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

#definimos las urls a ser utilizadas: 
# admin/, users/, receipts/.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
     path('receipts/', include('receipts.urls')),
]

#para enviar los archivos en el endpoint receipts/{id}/file (en desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)