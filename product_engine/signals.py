from django.db.models.signals import post_save
from django.dispatch import receiver
from product_engine.models import Product
from ai.models import Content
from ai.services import generate_hooks, generate_captions, generate_scripts

@receiver(post_save, sender=Product)
def generate_content(sender, instance, created, **kwargs):
    """
    Сигнал, який автоматично генерує AI‑контент після створення нового продукту.
    Викликається кожного разу, коли зберігається Product.
    """
    if created:
        try:
            # Генеруємо кілька варіантів контенту через AI‑сервіс
            hooks = generate_hooks(instance.title, count=10)       # 10 рекламних хуків
            captions = generate_captions(instance.title, count=5)  # 5 описів
            scripts = generate_scripts(instance.title, count=3)    # 3 сценарії

            # Зберігаємо всі варіанти у таблиці Content
            for hook in hooks:
                Content.objects.create(product=instance, hook=hook)

            for caption in captions:
                Content.objects.create(product=instance, problem_solution=caption)

            for script in scripts:
                Content.objects.create(product=instance, cta=script)

        except Exception as e:
            # Логування помилки, щоб сервер не падав при проблемах з API
            print(f"Помилка генерації контенту для {instance.title}: {e}")

