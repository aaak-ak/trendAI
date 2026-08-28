from django.contrib import admin
from product_engine.models import Product
from ai.models import Content
from ai.services import generate_hooks, generate_captions, generate_scripts

# Inline‑редагування контенту прямо всередині продукту
class ContentInline(admin.TabularInline):
    model = Content
    extra = 0
    fields = ("hook", "problem_solution", "cta", "hashtags", "trend", "created_at")
    readonly_fields = ("created_at",)

@admin.action(description="Згенерувати AI‑контент")
def generate_ai_content(modeladmin, request, queryset):
    for product in queryset:
        hooks = generate_hooks(product.title, count=3)
        captions = generate_captions(product.title, count=2)
        scripts = generate_scripts(product.title, count=1)

        Content.objects.create(product=product, hook=hooks[0])
        Content.objects.create(product=product, problem_solution=captions[0])
        Content.objects.create(product=product, cta=scripts[0])

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "has_content")
    list_editable = ("price",)
    search_fields = ("title",)
    list_filter = ("price",)
    ordering = ("title",)
    inlines = [ContentInline]
    actions = [generate_ai_content]  # кнопка для генерації контенту

    def has_content(self, obj):
        return Content.objects.filter(product=obj).exists()
    has_content.boolean = True
    has_content.short_description = "Has Content?"

