from product_engine.models import Product
from analytics.models import Analytics


def score(product: Product) -> str:

    scoring = product.scoring_result or 0

    if scoring >= 90:
        return "SCALE"

    elif scoring >= 70:
        return "TEST"

    else:
        return "KILL"

