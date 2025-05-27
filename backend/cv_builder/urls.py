from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cvs.urls", namespace = "cvs")),

    ]

# # Serve static and media files during development
# if settings.DEBUG:
#     # Serve media files (already in your code)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     # Serve static files
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
