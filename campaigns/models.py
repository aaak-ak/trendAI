from django.db import models

class Campaign(models.Model):
    trend = models.ForeignKey("trends.Trend", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    affiliate_url = models.URLField(blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

