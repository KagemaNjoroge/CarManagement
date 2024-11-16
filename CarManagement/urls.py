from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from CarManagement import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Car Management API",
        default_version="v1",
        description="CarManagementAPI Documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="user@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include("cars.urls")),
    path("auth/", include("authentication.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
