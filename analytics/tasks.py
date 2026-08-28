from celery import shared_task
from product_engine.models import Product
from analytics.scoring import score

@shared_task
def update_analytics():
    products = Product.objects.all()
    for p in products:
        decision = score(p)
        # можна зберігати рішення у моделі Product
        p.decision = decision
        p.save()
