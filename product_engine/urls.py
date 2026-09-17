from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # головна сторінка зі списком продуктів
    path("product/<int:pk>/", views.product_detail, name="product_detail"),  # деталі продукту
]

