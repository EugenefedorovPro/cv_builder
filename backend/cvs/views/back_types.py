from typing import TypedDict


# ----------------------------
# Common / nested serializer data
# ----------------------------

class ErrorResponseType(TypedDict):
    details: str


class PhotoData(TypedDict, total=False):
    photo_url: str | None


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


class HardSkillData(TypedDict):
    id: int
    category: str
    hard_skill_text: str


class ManifestData(TypedDict):
    id: int
    manifest_text: str


class ProjectData(TypedDict, total=False):
    id: int
    project_name: str
    project_text: str
    web_url: str | None
    git_url: str | None


class ExperienceData(TypedDict, total=False):
    id: int
    company: str
    start_date: str
    end_date: str | None
    achievements: str | None
    position: str


class SoftSkillData(TypedDict):
    id: int
    soft_skill_text: str


class EducationData(TypedDict):
    id: int
    institution: str
    degree_title: str
    start_date: str
    end_date: str


class InterestData(TypedDict, total=False):
    id: int
    interest_text: str | None


class NaturalLanguageData(TypedDict):
    id: int
    natural_lang: str
    level: str


# ----------------------------
# Block names for each view
# ----------------------------

class HeaderBlockNamesType(TypedDict, total=False):
    github_title: str | None
    linkedin_title: str | None
    country_title: str | None
    city_title: str | None
    district_title: str | None


class HardSkillBlockNamesType(TypedDict, total=False):
    hard_skills_name: str | None


class ManifestBlockNamesType(TypedDict, total=False):
    manifest_name: str | None


class ProjectBlockNamesType(TypedDict, total=False):
    project_name: str | None
    # Better logical alternative for future:
    # projects_name: str | None


class ExperienceBlockNamesType(TypedDict, total=False):
    experience_name: str | None
    company_title: str | None
    exp_period_title: str | None
    position_title: str | None
    achievements_title: str | None


class SoftSkillBlockNamesType(TypedDict, total=False):
    soft_skills_name: str | None


class EducationBlockNamesType(TypedDict, total=False):
    education_name: str | None


class InterestBlockNamesType(TypedDict, total=False):
    interest_name: str | None


class NaturalLangBlockNamesType(TypedDict, total=False):
    natural_lang_name: str | None


# ----------------------------
# Full success responses
# ----------------------------

class HeaderViewResponseType(TypedDict):
    block_names: HeaderBlockNamesType
    header: HeaderData


class HardSkillViewResponseType(TypedDict):
    block_names: HardSkillBlockNamesType
    hard_skills: list[HardSkillData]


class ManifestViewResponseType(TypedDict):
    block_names: ManifestBlockNamesType
    manifest: ManifestData


class ProjectViewResponseType(TypedDict):
    block_names: ProjectBlockNamesType
    projects: list[ProjectData]


class ExperienceViewResponseType(TypedDict):
    block_names: ExperienceBlockNamesType
    experience: list[ExperienceData]


class SoftSkillViewResponseType(TypedDict):
    block_names: SoftSkillBlockNamesType
    soft_skills: list[SoftSkillData]


class EducationViewResponseType(TypedDict):
    block_names: EducationBlockNamesType
    education: list[EducationData]


class InterestViewResponseType(TypedDict):
    block_names: InterestBlockNamesType
    interests: list[InterestData]


class NaturalLangViewResponseType(TypedDict):
    block_names: NaturalLangBlockNamesType
    natural_langs: list[NaturalLanguageData]
