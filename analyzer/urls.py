from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("analyze/", views.ImageUploadView.as_view())
]
