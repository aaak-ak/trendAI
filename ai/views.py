from django.shortcuts import render
from rest_framework import viewsets
from ai.models import Content
from ai.serializers import ContentSerializer
from .services import (
    generate_description,
    generate_hook,
    generate_hashtags,
    generate_scripts,
)
from product_engine.models import Product

# --- Django views для HTML ---
def ai_generate(request):

    products = Product.objects.all()

    if request.method == "POST":

        title = request.POST.get("title")

        description = generate_description(title)

        hook = generate_hook(title)

        hashtags = generate_hashtags(title)

        tiktok_script = generate_scripts(title)[0]

        product = Product.objects.filter(
            title=title
        ).first()

        if product:

            Content.objects.create(
               product=product,
               hook=hook,
               problem_solution=description,
               cta="Click the affiliate link to learn more.",
               tiktok_script=tiktok_script,
               hashtags=" ".join(hashtags)
            )

        return render(
            request,
            "ai/result.html",
            {
                "title": title,
                "description": description,
                "hook": hook,
                "hashtags": hashtags,
                "tiktok_script": tiktok_script
            }
        )

    return render(
        request,
        "ai/generate.html",
        {
            "products": products
        }
    )


def index(request):
    """
    Головна сторінка AI‑модуля.
    """
    return render(request, "ai/index.html")


# --- DRF endpoint для API ---
class ContentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для перегляду AI‑контенту.
    Повертає JSON зі списком контенту.
    """
    queryset = Content.objects.all().order_by("-created_at")
    serializer_class = ContentSerializer

