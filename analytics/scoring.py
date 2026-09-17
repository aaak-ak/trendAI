from product_engine.models import Product   # модель продукту
from analytics.models import Analytics      # модель аналітики (views, clicks)

def score(product: Product) -> str:
    """
    Обчислює рейтинг продукту на основі CTR, трендового балу та кліків.
    Повертає рішення: SCALE / TEST / KILL
    """

    # отримуємо перший об'єкт аналітики для продукту
    analytics = product.analytics.first()

    # обчислюємо CTR (clicks/views * 100), якщо є дані
    if analytics and analytics.views > 0:
        ctr = analytics.clicks / analytics.views * 100
        clicks = analytics.clicks
    else:
        ctr = 0
        clicks = 0

    # трендовий бал (якщо є поле у моделі Product)
    trend = getattr(product, "trend_score", 0)

    # формула з вагами
    score_value = ctr * 0.4 + trend * 0.4 + clicks * 0.2

    if score_value > 70:
        return "SCALE"
    elif score_value > 40:
        return "TEST"
    else:
        return "KILL"

