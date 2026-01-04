from django.urls import path
from .views import HealthView, LiveView, ReadyView

urlpatterns = [
    path("", HealthView.as_view(), name="health"),
    path("live/", LiveView.as_view(), name="live"),
    path("ready/", ReadyView.as_view(), name="ready"),
]
