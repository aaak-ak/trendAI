from django.shortcuts import render, get_object_or_404
from .models import Product
from analytics.models import Analytics

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # знайти або створити запис аналітики
    analytics, created = Analytics.objects.get_or_create(product=product)
    analytics.views += 1
    analytics.save(update_fields=["views"])

    return render(request, "products/detail.html", {"product": product})

def home(request):
    return render(request, "product_engine/home.html")