from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from product_engine.views import home, ProductViewSet
from rest_framework import routers
from analytics.views import AnalyticsViewSet
from trends.views import TrendViewSet, TrendCandidateViewSet

# Health check endpoint
def health_check(request):
    return JsonResponse({"status": "ok"})

# Router для DRF
router = routers.DefaultRouter()
router.register(r'product_engine', ProductViewSet)          # краще products, ніж product_engine
router.register(r'analytics', AnalyticsViewSet)
router.register(r'trends', TrendViewSet)
router.register(r'trend_candidates', TrendCandidateViewSet)

urlpatterns = [
    path("", home, name="home"),                       # головна сторінка
    path("ping/", health_check),                       # health endpoint
    path("admin/", admin.site.urls),                   # адмінка
    path("ai/", include(("ai.urls", "ai"), namespace="ai")),  # AI namespace
    path("product_engine/", include("product_engine.urls")),  # маршрути продуктів
    path("analytics/", include("analytics.urls")),     # маршрути аналітики
    path("traffic/", include("traffic.urls")),         # маршрути трафіку
    path("api/", include(router.urls)),
    path("api/", include(router.urls)),                                # API маршрути
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
