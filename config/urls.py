from django.contrib import admin
from django.urls import path, include, re_path  # re_path는 drf-yasg
from w2m import views
from django.conf import settings
from django.conf.urls.static import static

# 아래는 다 drf_yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


# drf_yasg설정
schema_url_patterns = [
    path("", include("w2m.urls")),
]
schema_view = get_schema_view(
    openapi.Info(
        title="Django API",
        default_version="v1",
        description="장고 예약 API",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    patterns=schema_url_patterns,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main, name="main"),
    path("", include("w2m.urls")),
    re_path(
        r"^swagger(?P<format>\.json|\.yam|)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
