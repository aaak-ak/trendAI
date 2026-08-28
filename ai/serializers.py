from rest_framework import serializers
from ai.models import Content

class ContentSerializer(serializers.ModelSerializer):
    """
    Serializer для моделі Content.
    Використовується у DRF ViewSet.
    """
    class Meta:
        model = Content
        fields = ["id", "product", "hook", "problem_solution", "cta", "hashtags", "trend", "created_at"]
