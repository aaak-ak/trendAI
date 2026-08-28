from django.contrib import admin
from ai.models import Content

@admin.register(Content)
class AIContentAdmin(admin.ModelAdmin):
    # Поля, які будуть показані у списку
    list_display = (
        "product",          # назва продукту
        "hook",             # хук
        "problem_solution", # опис проблеми/рішення
        "cta",              # заклик до дії
        "hashtags",         # хештеги
        "trend",            # тренд, якщо є
        "created_at",       # дата створення
    )

    # Поля, по яких можна робити пошук
    search_fields = ("product__title", "hook", "problem_solution", "cta", "hashtags")

    # Фільтри праворуч у адмінці
    list_filter = ("trend", "created_at")

    # Сортування за замовчуванням
    ordering = ("-created_at",)

    # Кількість записів на сторінку
    list_per_page = 20


