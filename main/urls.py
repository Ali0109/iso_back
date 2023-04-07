from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from . import views
from .settings import base

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/app/', include('api.urls_app')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': base.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': base.STATIC_ROOT}),
]

urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
urlpatterns += static(base.STATIC_URL, document_root=base.STATIC_ROOT)
