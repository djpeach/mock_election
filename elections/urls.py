from django.urls import path
from . import views

urlpatterns = [
    path("", views.results, name="results"),
    path("vote", views.vote, name="vote"),
]
