from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cvs.urls", namespace = "cvs")),

    path(
        'token/',
        jwt_views.TokenObtainPairView.as_view(),
        name = 'token_obtain_pair'
        ),

    path(
        'token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name = 'token_refresh'
        ),
    ]

# # Serve static and media files during development
# if settings.DEBUG:
#     # Serve media files (already in your code)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     # Serve static files
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
