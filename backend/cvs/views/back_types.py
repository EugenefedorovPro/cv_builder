from datetime import date, datetime
from typing import TypedDict


class HeaderPhotoType(TypedDict, total=False):
    photo_url: str | None


class HeaderData(TypedDict, total=False):
    id: int
    photo: HeaderPhotoType | None
    first_name: str
    second_name: str
    phone: str
    email: str
    linkedin: str | None
    github: str | None
    country: str | None
    city: str | None
    district: str | None


class CustomUserData(TypedDict, total=False):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    is_active: bool
    is_staff: bool
    is_superuser: bool


class LanguageChoiceData(TypedDict):
    lang: str


class OccupationChoiceData(TypedDict):
    occupation: str


class BlockNamesData(TypedDict, total=False):
    photo_name: str | None
    header_name: str | None
    hard_skills_name: str | None
    manifest_name: str | None
    projects_name: str | None
    experience_name: str | None
    soft_skills_name: str | None
    education_name: str | None
    natural_lang_name: str | None
    interest_name: str | None
    cases_name: str | None
    why_me_name: str | None
    feedback_name: str | None

    lang_id: int
    user_id: int
    occupation_id: int

    github_title: str | None
    linkedin_title: str | None
    country_title: str | None
    city_title: str | None
    district_title: str | None

    company_title: str | None
    exp_period_title: str | None
    position_title: str | None
    achievements_title: str | None

    institution_title: str | None
    ed_period_title: str | None
    degree_title: str | None

    level_title: str | None

    task_title: str | None
    solution_title: str | None
    optimization_title: str | None
    result_title: str | None
    tech_stack_title: str | None

    contacts_title: str | None
    current: str | None


class PhotosData(TypedDict, total=False):
    photo_url: str | None
    description: str | None
    user_id: int
    lang_id: int
    occupation_id: int


class ManifestData(TypedDict):
    manifest_text: str
    lang_id: int
    user_id: int
    occupation_id: int


class HardSkillData(TypedDict):
    category: str
    hard_skill_text: str
    lang_id: int
    user_id: int
    occupation_id: int


class ProjectData(TypedDict, total=False):
    project_name: str
    project_text: str
    web_url: str | None
    git_url: str | None
    lang_id: int
    user_id: int
    occupation_id: int


class ExperienceData(TypedDict, total=False):
    company: str
    start_date: date
    end_date: date | None
    position: str
    achievements: str | None
    order: int
    lang_id: int
    user_id: int
    occupation_id: int


class SoftSkillData(TypedDict):
    soft_skill_text: str
    lang_id: int
    user_id: int
    occupation_id: int


class EducationData(TypedDict):
    institution: str
    start_date: date
    end_date: date
    degree_title: str
    lang_id: int
    user_id: int
    occupation_id: int


class NaturalLanguageData(TypedDict):
    natural_lang: str
    level: str
    lang_id: int
    user_id: int
    occupation_id: int


class InterestData(TypedDict):
    interest_text: str
    lang_id: int
    user_id: int
    occupation_id: int


class CaseData(TypedDict, total=False):
    task: str
    solution: str
    optimization: str | None
    result: str | None
    tech_stack: str
    lang_id: int
    user_id: int
    occupation_id: int


class WhyMeData(TypedDict):
    company: str
    why_me_text: str
    lang_id: int
    user_id: int
    occupation_id: int


class FeedbackData(TypedDict, total=False):
    company: str
    feedback_text: str
    contacts: str | None
    lang_id: int
    user_id: int
    occupation_id: int
