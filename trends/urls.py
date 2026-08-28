from django.urls import path
from trends import views

urlpatterns = [
    path("add/", views.add_trend, name="add_trend"),
    path("list/", views.trend_list, name="trend_list"),
]