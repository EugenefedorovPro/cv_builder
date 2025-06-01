from django.urls import path
from .views import HeaderView, HardSkillView

app_name = "cvs"

urlpatterns = [
    path("header/", HeaderView.as_view(), name = "header"),
    path("hard_skills/", HardSkillView.as_view(), name = "hard_skills"),

    ]
