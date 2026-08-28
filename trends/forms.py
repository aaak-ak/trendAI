from django import forms
from trends.models import Trend

class TrendForm(forms.ModelForm):
    """
    Форма для створення/редагування тренду вручну.
    Використовується у views та шаблонах.
    """
    class Meta:
        model = Trend
        fields = ["name", "source", "popularity"]
