from django.shortcuts import render, get_object_or_404, redirect
from product_engine.models import Product
from analytics.scoring import score
from .models import Click, Analytics
from .serializers import AnalyticsSerializer
from rest_framework import viewsets

class AnalyticsViewSet(viewsets.ModelViewSet):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer


def dashboard(request):
    # Отримуємо всі продукти
    products = Product.objects.all()

    # Формуємо список даних для шаблону
    data = []
    for p in products:
        # беремо перший об'єкт аналітики для продукту (або None)
        analytics = p.analytics.first()

        # обчислюємо CTR на льоту (clicks/views * 100)
        ctr = (analytics.clicks / analytics.views * 100) if analytics and analytics.views > 0 else 0
        clicks = analytics.clicks if analytics else 0

        data.append({
            "title": p.title,
            "ctr": ctr,
            "clicks": clicks,
            "decision": score(p)
        })

    # Підрахунок для summary
    summary = {
        "scale": sum(1 for d in data if d["decision"] == "SCALE"),
        "test": sum(1 for d in data if d["decision"] == "TEST"),
        "kill": sum(1 for d in data if d["decision"] == "KILL"),
    }

    # Передаємо дані у шаблон
    return render(request, "analytics/dashboard.html", {
        "products": data,
        "summary": summary
    })


def track_click(request, pk):
    click = get_object_or_404(Click, pk=pk)
    # Логіка: збільшити лічильник кліків
    click.count += 1
    click.save()
    # Перенаправити користувача на збережений URL
    return redirect(click.url)

