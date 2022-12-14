
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from autosapp.api.router import router_vehiculos

from autosapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("autosapp.urls")),
    path('api/', include(router_vehiculos.urls))
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)