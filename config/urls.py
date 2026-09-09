from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from product_engine.views import home, ProductViewSet
from rest_framework import routers
from analytics.views import AnalyticsViewSet
from trends.views import TrendViewSet


router = routers.DefaultRouter()
router.register(r'product_engine', ProductViewSet)
router.register(r'analytics', AnalyticsViewSet)
router.register(r'trends', TrendViewSet)


def health_check(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("", home, name="home"),   # головна сторінка
    path("ping/", health_check),   # health endpoint
    path("admin/", admin.site.urls),
    path("ai/", include(("ai.urls", "ai"), namespace="ai")),  # правильний синтаксис для namespace
    path("", include("product_engine.urls")),
    path("analytics/", include("analytics.urls")),
    path("traffic/", include("traffic.urls")),
    path("api/", include(router.urls)),   # API маршрути
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
