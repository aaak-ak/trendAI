from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    scoring_result = models.FloatField(null=True, blank=True)

    # універсальні поля для монетизації
    platform = models.CharField(
        max_length=50,
        choices=[
            ("Amazon", "Amazon"),
            ("AliExpress", "AliExpress"),
            ("eBay", "eBay"),
            ("Etsy", "Etsy"),
        ],
        default="Amazon"
    )

    # окремі ID для кожної платформи
    asin = models.CharField(max_length=20, blank=True, null=True)       # Amazon ASIN
    aliexpress_id = models.CharField(max_length=50, blank=True, null=True)
    ebay_id = models.CharField(max_length=50, blank=True, null=True)
    etsy_id = models.CharField(max_length=50, blank=True, null=True)

    affiliate_link = models.CharField(max_length=500, blank=True, null=True)  # партнерське посилання
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        # генеруємо affiliate_link тільки якщо воно пусте
        if not self.affiliate_link:
            if self.platform == "Amazon" and self.asin:
                self.affiliate_link = f"https://www.amazon.de/dp/{self.asin}?tag=trendai-21"
            elif self.platform == "AliExpress" and self.aliexpress_id:
                self.affiliate_link = f"https://www.aliexpress.com/item/{self.aliexpress_id}.html?aff_id=YOUR_ID"
            elif self.platform == "eBay" and self.ebay_id:
                self.affiliate_link = f"https://www.ebay.com/itm/{self.ebay_id}?campid=YOUR_ID"
            elif self.platform == "Etsy" and self.etsy_id:
                self.affiliate_link = f"https://www.etsy.com/listing/{self.etsy_id}?ref=YOUR_ID"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.platform})"


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

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} → {self.product.title}"
