from django.shortcuts import render, redirect, get_object_or_404
from trends.forms import TrendForm
from trends.models import Trend, TrendCandidate
from rest_framework import viewsets
from .serializers import TrendSerializer, TrendCandidateSerializer

# API ViewSets
class TrendViewSet(viewsets.ModelViewSet):
    queryset = Trend.objects.all()
    serializer_class = TrendSerializer

class TrendCandidateViewSet(viewsets.ModelViewSet):
    queryset = TrendCandidate.objects.all()
    serializer_class = TrendCandidateSerializer


# Function-based views (для форм і HTML)
def add_trend(request):
    """
    View для додавання нового тренду вручну.
    Якщо POST — зберігаємо тренд, якщо GET — показуємо форму.
    """
    if request.method == "POST":
        form = TrendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("trend_list")  # після збереження йдемо на список трендів
    else:
        form = TrendForm()
    return render(request, "trends/add_trend.html", {"form": form})


def trend_list(request):
    """
    View для перегляду всіх трендів.
    """
    trends = Trend.objects.all().order_by("-created_at")
    return render(request, "trends/list_trends.html", {"trends": trends})

