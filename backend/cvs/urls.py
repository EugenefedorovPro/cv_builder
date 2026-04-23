from django.urls import path

from cvs.views.component_views import (
    EducationView,
    ExperienceView,
    HardSkillView,
    HeaderView,
    InterestView,
    ManifestView,
    NaturalLangView,
    OccupationChoiceView,
    ProjectView,
    SignUpView,
    SoftSkillView,
)
from cvs.views.generate_docx_view import GenerateDocx

app_name = "cvs"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("occupation_choice/", OccupationChoiceView.as_view(), name="occupation_choice"),
    path("header/", HeaderView.as_view(), name="header"),
    path("hard_skills/", HardSkillView.as_view(), name="hard_skills"),
    path("manifest/", ManifestView.as_view(), name="manifest"),
    path("projects/", ProjectView.as_view(), name="projects"),
    path("experience/", ExperienceView.as_view(), name="experience"),
    path("soft_skills/", SoftSkillView.as_view(), name="soft_skills"),
    path("education/", EducationView.as_view(), name="education"),
    path("interest/", InterestView.as_view(), name="interest"),
    path("natural_lang/", NaturalLangView.as_view(), name="natural_lang"),
    path("generate_docx/", GenerateDocx.as_view(), name="generate_docx"),
]
