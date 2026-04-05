from typing import TypedDict


class ErrorResponseType(TypedDict):
    details: str


# Header
class PhotoData(TypedDict, total=False):
    photo_url: str | None


class HeaderBlockNamesType(TypedDict, total=False):
    github_title: str | None
    linkedin_title: str | None
    country_title: str | None
    city_title: str | None
    district_title: str | None


class HeaderData(TypedDict, total=False):
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
class HardSkillBlockNamesType(TypedDict, total=False):
    hard_skills_name: str | None


class HardSkillData(TypedDict):
    id: int
    category: str
    hard_skill_text: str


class HardSkillViewResponseType(TypedDict):
    block_names: HardSkillBlockNamesType
    hard_skills: list[HardSkillData]


# Manifest
class ManifestBlockNamesType(TypedDict, total=False):
    manifest_name: str | None


class ManifestData(TypedDict):
    id: int
    manifest_text: str


class ManifestViewResponseType(TypedDict):
    block_names: ManifestBlockNamesType
    manifest: ManifestData


class ProjectBlockNamesType(TypedDict, total=False):
    project_name: str | None
    # Better logical alternative for future:
    # projects_name: str | None


class ProjectData(TypedDict, total=False):
    id: int
    project_name: str
    project_text: str
    web_url: str | None
    git_url: str | None


class ProjectViewResponseType(TypedDict):
    block_names: ProjectBlockNamesType
    projects: list[ProjectData]


class ExperienceBlockNamesType(TypedDict, total=False):
    experience_name: str | None
    company_title: str | None
    exp_period_title: str | None
    position_title: str | None
    achievements_title: str | None


class ExperienceData(TypedDict, total=False):
    id: int
    company: str
    start_date: str
    end_date: str | None
    achievements: str | None
    position: str


class ExperienceViewResponseType(TypedDict):
    block_names: ExperienceBlockNamesType
    experience: list[ExperienceData]


class SoftSkillBlockNamesType(TypedDict, total=False):
    soft_skills_name: str | None


class SoftSkillData(TypedDict):
    id: int
    soft_skill_text: str


class SoftSkillViewResponseType(TypedDict):
    block_names: SoftSkillBlockNamesType
    soft_skills: list[SoftSkillData]


class EducationBlockNamesType(TypedDict, total=False):
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


class InterestBlockNamesType(TypedDict, total=False):
    interest_name: str | None


class InterestData(TypedDict, total=False):
    id: int
    interest_text: str | None


class InterestViewResponseType(TypedDict):
    block_names: InterestBlockNamesType
    interests: list[InterestData]


class NaturalLangBlockNamesType(TypedDict, total=False):
    natural_lang_name: str | None


class NaturalLanguageData(TypedDict):
    id: int
    natural_lang: str
    level: str


class NaturalLangViewResponseType(TypedDict):
    block_names: NaturalLangBlockNamesType
    natural_langs: list[NaturalLanguageData]


class CustomUserType(TypedDict):
    id: int
    username: str
    first_name: str | None
    second_name: str | None
    email: str

class UserResponseType(TypedDict):
    user_data: CustomUserType
