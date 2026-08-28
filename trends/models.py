from django.db import models

class TrendCandidate(models.Model):
    title = models.CharField(max_length=255)
    trend_score = models.IntegerField(default=0)
    source = models.CharField(max_length=50, default="aliexpress")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.trend_score})"


class Trend(models.Model):
    name = models.CharField(max_length=255)
    source = models.CharField(max_length=255, blank=True, null=True)
    popularity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name