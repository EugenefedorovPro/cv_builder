from django.urls import path
from .views import (HeaderView,
                    HardSkillView,
                    ManifestView,
                    ProjectView,
                    SoftSkillView,
                    EducationView,
                    ExperienceView,
                    InterestView,
                    )

app_name = "cvs"

urlpatterns = [
    path("header/", HeaderView.as_view(), name = "header"),
    path("hard_skills/", HardSkillView.as_view(), name = "hard_skills"),
    path("manifest/", ManifestView.as_view(), name = "manifest"),
    path("projects/", ProjectView.as_view(), name = "projects"),
    path("experience/", ExperienceView.as_view(), name = "experience"),
    path("soft_skills/", SoftSkillView.as_view(), name = "soft_skills"),
    path("education/", EducationView.as_view(), name = "education"),
    path("interest/", InterestView.as_view(), name = "interest"),

    ]
