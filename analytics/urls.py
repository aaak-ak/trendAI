from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("click/<int:pk>/", views.track_click, name="track_click"),
]

