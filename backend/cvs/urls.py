from django.urls import path
from .views import (HeaderView,
                    HardSkillView,
                    ManifestView, ProjectView,
                    )

app_name = "cvs"

urlpatterns = [
    path("header/", HeaderView.as_view(), name = "header"),
    path("hard_skills/", HardSkillView.as_view(), name = "hard_skills"),
    path("manifest/", ManifestView.as_view(), name = "manifest"),
    path("projects/", ProjectView.as_view(), name = "projects"),

    ]
