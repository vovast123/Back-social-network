from django.contrib import admin
from django.urls import path,include
from .aysg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ksp.urls')),
]

urlpatterns += doc_urls