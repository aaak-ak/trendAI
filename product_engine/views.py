from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from ai.models import Content

from .models import Product
from .serializers import ProductSerializer

from analytics.models import Analytics
from ai.models import Content


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def home(request):

    products = Product.objects.all()

    products_count = Product.objects.count()

    content_count = Content.objects.count()

    winners_count = 0

    total_clicks = 0

    for product in products:

        analytics = Analytics.objects.filter(
            product=product
        ).first()

        if analytics:

            total_clicks += analytics.clicks

            ctr = 0

            if analytics.views > 0:

                ctr = (
                    analytics.clicks /
                    analytics.views
                ) * 100

            if ctr > 5:

                winners_count += 1

    context = {

        "products": products,

        "products_count": products_count,

        "content_count": content_count,

        "winners_count": winners_count,

        "total_clicks": total_clicks,

    }

    return render(
        request,
        "product_engine/home.html",
        context
    )


def product_detail(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    analytics, created = Analytics.objects.get_or_create(
        product=product
    )

    analytics.views += 1

    analytics.save(
        update_fields=["views"]
    )

    latest_content = Content.objects.first()

    return render(
        request,
        "product_engine/detail.html",
        {
            "product": product,
            "content": latest_content
        }
    )