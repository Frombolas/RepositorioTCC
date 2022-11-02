
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.tcc.urls')),
    path("autor/", include('apps.autor.urls')),
    path('accounts/',include('apps.acocounts.urls')),
    path("orientador/", include('apps.orientador.urls')),
    path("curso/", include('apps.curso.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
