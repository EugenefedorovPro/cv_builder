from django.urls import path
from .views import HeaderView

app_name = "cvs"

urlpatterns = [
    path("header/", HeaderView.as_view(), name = "header"),

    ]
