from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    scoring_result = models.FloatField(null=True, blank=True)

    # нові поля для монетизації
    affiliate_link = models.URLField(blank=True, null=True)  # партнерське посилання
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Content(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="engine_content")
    hook = models.TextField()
    caption = models.TextField()
    video_script = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Engine Content for {self.product.title}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorited_by")
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'product')  # один користувач не може додати той самий товар двічі

    def __str__(self):
        return f"{self.user.username} → {self.product.title}"
