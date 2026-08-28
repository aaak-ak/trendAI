from django.db import models
from product_engine.models import Product

class Analytics(models.Model):
    product = models.ForeignKey("product_engine.Product", on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    conversions = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def ctr(self):
        return (self.clicks / self.views) * 100 if self.views else 0

class Click(models.Model):
    url = models.URLField()
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.url} ({self.count})"