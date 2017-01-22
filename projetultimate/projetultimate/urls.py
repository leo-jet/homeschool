from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from terminalS import urls_terminals
from django.conf.urls.static import static

urlpatterns = [
    url(r'^terminals/', include(urls_terminals)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
