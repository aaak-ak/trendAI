from product_engine.models import Product   # модель продукту
from analytics.models import Analytics      # модель аналітики (views, clicks, ctr)

def score(product: Product) -> str:
    """
    Обчислює рейтинг продукту на основі CTR, трендового балу та кліків.
    Повертає рішення: SCALE / TEST / KILL
    """

    # отримуємо дані з пов'язаних моделей
    ctr = product.analytics.ctr if hasattr(product, "analytics") else 0
    trend = getattr(product, "trend_score", 0)
    clicks = product.analytics.clicks if hasattr(product, "analytics") else 0

    # формула з вагами
    score_value = ctr * 0.4 + trend * 0.4 + clicks * 0.2

    if score_value > 70:
        return "SCALE"
    elif score_value > 40:
        return "TEST"
    else:
        return "KILL"
