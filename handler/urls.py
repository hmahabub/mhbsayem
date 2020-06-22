from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="homepage"),
    path("portfolio", views.portfolio, name="Portfolio"),
    path("send", views.save, name = "SaveMessage"),
    path("check/message", views.messages, name="message"),
    ]