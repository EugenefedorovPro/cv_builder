from collections import namedtuple
from typing import NotRequired, TypedDict

DATE_FORMATTER = "%Y-%m-%d"


class ErrorResponseType(TypedDict):
    details: str


# Header
class PhotoData(TypedDict):
    photo_url: str


class HeaderBlockNamesType(TypedDict):
    github_title: str | None
    linkedin_title: str | None
    country_title: str | None
    city_title: str | None
    district_title: str | None


class HeaderData(TypedDict):
    id: int
    photo: PhotoData | None
    first_name: str
    second_name: str
    phone: str
    email: str
    linkedin: str | None
    github: str | None
    country: str | None
    city: str | None
    district: str | None


class HeaderViewResponseType(TypedDict):
    block_names: HeaderBlockNamesType
    header: HeaderData


# HardSkill
class HardSkillBlockNamesType(TypedDict):
    hard_skills_name: str | None


class HardSkillData(TypedDict):
    id: int
    category: str
    hard_skill_text: str


class HardSkillViewResponseType(TypedDict):
    block_names: HardSkillBlockNamesType
    hard_skills: list[HardSkillData]


# Manifest
class ManifestBlockNamesType(TypedDict):
    manifest_name: str | None


class ManifestData(TypedDict):
    id: int
    manifest_text: str


class ManifestViewResponseType(TypedDict):
    block_names: ManifestBlockNamesType
    manifest: ManifestData


class ProjectBlockNamesType(TypedDict):
    project_name: str | None
    # Better logical alternative for future:
    # projects_name: str | None


class ProjectData(TypedDict):
    id: int
    project_name: str
    project_text: str
    web_url: str | None
    git_url: str | None


class ProjectViewResponseType(TypedDict):
    block_names: ProjectBlockNamesType
    projects: list[ProjectData]


class ExperienceBlockNamesType(TypedDict):
    experience_name: str | None
    company_title: str | None
    exp_period_title: str | None
    position_title: str | None
    achievements_title: str | None


class ExperienceData(TypedDict):
    id: int
    company: str
    start_date: str
    end_date: str | None
    achievements: str | None
    position: str


class ExperienceViewResponseType(TypedDict):
    block_names: ExperienceBlockNamesType
    experience: list[ExperienceData]


class SoftSkillBlockNamesType(TypedDict):
    soft_skills_name: str | None


class SoftSkillData(TypedDict):
    id: int
    soft_skill_text: str


class SoftSkillViewResponseType(TypedDict):
    block_names: SoftSkillBlockNamesType
    soft_skills: list[SoftSkillData]


class EducationBlockNamesType(TypedDict):
    education_name: str | None


class EducationData(TypedDict):
    id: int
    institution: str
    degree_title: str
    start_date: str
    end_date: str


class EducationViewResponseType(TypedDict):
    block_names: EducationBlockNamesType
    education: list[EducationData]


class InterestBlockNamesType(TypedDict):
    interest_name: str | None


class InterestData(TypedDict):
    id: int
    interest_text: str | None


class InterestViewResponseType(TypedDict):
    block_names: InterestBlockNamesType
    interests: list[InterestData]


class NaturalLangBlockNamesType(TypedDict):
    natural_lang_name: str | None


class NaturalLanguageData(TypedDict):
    id: int
    natural_lang: str
    level: str


class NaturalLangViewResponseType(TypedDict):
    block_names: NaturalLangBlockNamesType
    natural_langs: list[NaturalLanguageData]


class CustomUserType(TypedDict):
    id: int | str
    username: str
    email: str
    password: NotRequired[ str | None]


class UserResponseType(TypedDict):
    user_data: CustomUserType


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
