from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from eventManager import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("eventManager.accounts.urls")),
    path("", include("eventManager.common.urls")),
    path("events/", include("eventManager.events.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
