from django.db import models
from product_engine.models import Product
from trends.models import Trend   # імпортуємо модель Trend з додатку trends

class Content(models.Model):
    # Зв’язок із продуктом: кожен контент належить конкретному продукту
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Основні блоки AI‑контенту
    hook = models.TextField(blank=True, null=True)              # рекламний хук
    problem_solution = models.TextField(blank=True, null=True)  # опис проблеми та рішення
    cta = models.TextField(blank=True, null=True)               # заклик до дії (Call To Action)
    hashtags = models.TextField(blank=True, null=True)          # список хештегів

    # Прив’язка до тренду (може бути пустою)
    trend = models.ForeignKey(Trend, on_delete=models.SET_NULL, null=True, blank=True)

    # Дата створення запису
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Сортування за датою створення (новіші зверху)
        ordering = ["-created_at"]
        # Назви для адмінки
        verbose_name = "AI Content"
        verbose_name_plural = "AI Contents"
        # Індекси для швидкого пошуку по продукту та тренду
        indexes = [
            models.Index(fields=["product"]),
            models.Index(fields=["trend"]),
        ]

    def __str__(self):
        # У адмінці буде видно назву продукту та тренд (якщо є)
        return f"{self.product.title} — {self.trend.name if self.trend else 'No Trend'}"


