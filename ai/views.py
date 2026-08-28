from django.shortcuts import render
from rest_framework import viewsets
from ai.models import Content
from ai.serializers import ContentSerializer
from .services import generate_description, generate_hook, generate_hashtags

# --- Django views для HTML ---
def ai_generate(request):
    """
    View для генерації контенту через форму.
    Використовується у шаблонах generate.html та result.html.
    """
    if request.method == "POST":
        title = request.POST.get("title")
        description = generate_description(title)
        hook = generate_hook(title)
        hashtags = generate_hashtags(title)
        return render(request, "ai/result.html", {
            "title": title,
            "description": description,
            "hook": hook,
            "hashtags": hashtags
        })
    return render(request, "ai/generate.html")


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

