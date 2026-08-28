from django.contrib import admin
from .models import Trend, TrendCandidate

@admin.register(Trend)
class TrendAdmin(admin.ModelAdmin):
    list_display = ("name", "source", "popularity", "created_at")
    search_fields = ("name",)
    list_filter = ("source", "popularity")

@admin.register(TrendCandidate)
class TrendCandidateAdmin(admin.ModelAdmin):
    list_display = ("title", "trend_score", "source", "created_at")
    search_fields = ("title",)
    list_filter = ("source", "trend_score")


