from django.urls import path
from . import views

urlpatterns = [
    path("go/<int:pk>/", views.go_redirect, name="go_redirect"),
]
