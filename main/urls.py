from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from . import views, settings

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/app/', include('api.urls_app')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
