from django.db.models.signals import post_save
from django.dispatch import receiver
from product_engine.models import Product
from ai.models import Content
from ai.services import (
    generate_hook,
    generate_problem_solution,
    generate_cta,
    generate_hashtags,
)

@receiver(post_save, sender=Product)
def create_ai_content(sender, instance, created, **kwargs):
    """
    Автоматично створює AI‑контент для нового продукту.
    Викликається після збереження Product.
    """
    if created:
        try:
            Content.objects.create(
                product=instance,
                hook=generate_hook(instance.title),
                problem_solution=generate_problem_solution(instance.title),
                cta=generate_cta(instance.title),
                hashtags=" ".join(generate_hashtags(instance.title)),
            )
        except Exception as e:
            # Логування помилки, щоб не падало весь сервер
            print(f"Помилка генерації контенту для {instance.title}: {e}")

