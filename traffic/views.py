from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.db.models import F
from product_engine.models import Product
from analytics.models import Analytics

def go_redirect(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # збільшуємо кліки атомарно
    Analytics.objects.filter(product=product).update(clicks=F("clicks") + 1)
    return redirect(product.affiliate_url)

