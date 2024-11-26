from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("eventManager.accounts.urls")),
    path("", include("eventManager.common.urls")),
    path("events/", include("eventManager.events.urls")),
]
