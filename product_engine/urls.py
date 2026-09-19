from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="product_list"),  # список продуктів
    path("<int:pk>/", views.product_detail, name="product_detail"),  # деталі продукту
]
