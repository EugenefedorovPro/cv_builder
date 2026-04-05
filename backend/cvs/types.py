from collections import namedtuple
from typing import TypedDict

from cvs.models.models import OccupationChoice

DATE_FORMATTER = "%Y-%m-%d"

PhotoTuple = namedtuple(
    "PhotoTuple",
    (
        "id",
        "description",
        "name",
        "width",
        "height",
        "color",
        "mode",
        "format",
    ),
)

HeaderTuple = namedtuple(
    "HeaderTuple",
    (
        "id",
        "first_name",
        "second_name",
        "phone",
        "email",
        "linkedin",
        "github",
        "country",
        "city",
        "district",
    ),
    defaults=(
        None,
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ),
)

OccupationChoiceTuple = namedtuple(
    "OccupationChoiceTuple",
    (
        "id",
        "occupation",
    ),
)

ManifestTuple = namedtuple(
    "ManifestTuple",
    (
        "id",
        "manifest_text",
    ),
)

ProjectTuple = namedtuple(
    "ProjectTuple",
    (
        "project_name",
        "project_text",
        "web_url",
        "git_url",
    ),
)

ExperienceTuple = namedtuple(
    "ExperienceTuple",
    (
        "id",
        "company",
        "start_date",
        "end_date",
        "position",
        "achievements",
        "order",
    ),
)

HardSkillTuple = namedtuple(
    "HardSkillTuple",
    (
        "id",
        "category",
        "hard_skill_text",
    ),
)

SoftSkillTuple = namedtuple(
    "SoftSkillTuple",
    (
        "id",
        "soft_skill_text",
    ),
)

EducationTuple = namedtuple(
    "EducationTuple",
    (
        "id",
        "institution",
        "start_date",
        "end_date",
        "degree_title",
    ),
)

InterestTuple = namedtuple(
    "InterestTuple",
    (
        "id",
        "interest_text",
    ),
)

NaturalLangTuple = namedtuple(
    "NaturalLangTuple",
    (
        "id",
        "natural_lang",
        "level",
    ),
)


BlockNameTuple = namedtuple(
    "BlockNameTuple",
    (
        "id",
        "photo_name",
        "header_name",
        "hard_skills_name",
        "manifest_name",
        "projects_name",
        "experience_name",
        "soft_skills_name",
        "education_name",
        "natural_lang_name",
        "interest_name",
        "cases_name",
        "why_me_name",
        "feedback_name",
        "country_title",
        "github_title",
        "linkedin_title",
        "city_title",
        "district_title",
        "company_title",
        "exp_period_title",
        "position_title",
        "achievements_title",
        "institution_title",
        "ed_period_title",
        "degree_title",
        "level_title",
        "task_title",
        "solution_title",
        "optimization_title",
        "result_title",
        "tech_stack_title",
        "contacts_title",
        "current",
    ),
)
