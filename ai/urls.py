from django.urls import path, include
from rest_framework import routers
from ai.views import ContentViewSet, ai_generate, index

app_name = "ai"

# DRF router для API
router = routers.DefaultRouter()
router.register(r"content", ContentViewSet)

urlpatterns = [
    # HTML views
    path("", index, name="index"),
    path("generate/", ai_generate, name="ai_generate"),

    # API endpoint
    path("api/", include(router.urls)),
]
