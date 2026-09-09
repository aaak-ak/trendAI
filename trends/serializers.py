from rest_framework import serializers
from .models import Trend, TrendCandidate

class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = '__all__'

class TrendCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendCandidate
        fields = '__all__'

