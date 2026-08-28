from django.shortcuts import render
from product_engine.models import Product
from analytics.scoring import score
from django.shortcuts import get_object_or_404, redirect
from .models import Click

def dashboard(request):
    # Отримуємо всі продукти
    products = Product.objects.all()

    # Формуємо список даних для шаблону
    data = []
    for p in products:
        data.append({
            "title": p.title,
            "ctr": p.analytics.ctr if hasattr(p, "analytics") else 0,
            "clicks": p.analytics.clicks if hasattr(p, "analytics") else 0,
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
