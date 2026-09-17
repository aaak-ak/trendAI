from django.shortcuts import render, get_object_or_404
from .models import Product
from analytics.models import Analytics
from rest_framework import viewsets
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def home(request):
    # отримуємо всі продукти
    products = Product.objects.all()
    return render(request, "product_engine/home.html", {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # знайти або створити запис аналітики
    analytics, created = Analytics.objects.get_or_create(product=product)
    analytics.views += 1
    analytics.save(update_fields=["views"])

    return render(request, "product_engine/detail.html", {"product": product})
