from typing import TypedDict
from datetime import datetime
from collections import namedtuple

from cvs.models.models import OccupationChoice

DATE_FORMATTER = "%Y-%m-%d"

PhotoTuple = namedtuple("PhotoTuple", (
    "id",
    "description",
    "name",
    "width",
    "height",
    "color",
    "mode",
    "format",
    ))

HeaderTuple = namedtuple("HeaderTuple", (
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
    ))

OccupationChoiceTuple = namedtuple("OccupationChoiceTuple", (
    "id",
    "occupation",
    ))

ManifestTuple = namedtuple("ManifestTuple", (
    "id",
    "manifest_text",

    ))

ProjectTuple = namedtuple("ProjectTuple", (
    "project_name",
    "project_text",
    "web_url",
    "git_url",

    ))

ExperienceTuple = namedtuple("ExperienceTuple", (
    "id",
    "company",
    "start_date",
    "end_date",
    "position",
    "achievements",
    "order",

    ))

HardSkillTuple = namedtuple("HardSkillTuple", (
    "id",
    "category",
    "hard_skill_text",
    ))

SoftSkillTuple = namedtuple("SoftSkillTuple", (
    "id",
    "soft_skill_text",
    ))

EducationTuple = namedtuple("EducationTuple", (
    "id",
    "institution",
    "start_date",
    "end_date",
    "degree_title",
    ))

InterestTuple = namedtuple("InterestTuple", (
    "id",
    "interest_text",
    ))

NaturalLangTuple = namedtuple("NaturalLangTuple", (
    "id",
    "natural_lang",
    "level",

    ))

BlockNameTuple = namedtuple("BlockNameTuple", (
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

    ))


class BlockNameType(TypedDict):
    id: int
    photo_name: str
    header_name: str
    hard_skills_name: str
    manifest_name: str
    projects_name: str
    experience_name: str
    soft_skills_name: str
    education_name: str
    natural_lang_name: str
    interest_name: str
    cases_name: str
    why_me_name: str
    feedback_name: str


class PhotoType(TypedDict):
    id: str
    description: str
    name: str
    width: int
    height: int
    color: str
    mode: str
    format: str


class HeaderType(TypedDict):
    first_name: str
    second_name: str
    phone: str
    email: str
    linkedin: str
    github: str
    country: str | None
    city: str | None
    district: str | None


CvHeaderType = tuple[BlockNameType, list[HeaderType]]

class ManifestType(TypedDict):
    id: int
    manifest_text: str

CvManifestType = tuple[BlockNameType, list[ManifestType]]

class ProjectItemType(TypedDict):
    id: int
    project_name: str
    project_text: str
    web_url: str
    git_url: str


CvProjectType = tuple[BlockNameType, list[ProjectItemType]]


class ExperienceItemType(TypedDict):
    id: int
    company: str
    start_date: datetime
    end_date: datetime | None
    achievements: str
    position: str


CvExperienceType = tuple[BlockNameType, list[ExperienceItemType]]


class HardSkilItemType(TypedDict):
    id: int
    category: str
    hard_skill_text: str


CvHardSkillsType = tuple[BlockNameType, HardSkilItemType]


class SoftSkillItemType:
    id: int
    soft_skill_text: str


CvSoftSkillsType = tuple[BlockNameType, SoftSkillItemType]


class EducationItemType:
    id: int
    institution: str
    start_date: datetime
    end_date: datetime
    degree_title: str


CvEducationType = tuple[BlockNameType, EducationItemType]


class InterestItemType:
    id: int
    interest_text: str


CvInterestType = tuple[BlockNameType, InterestItemType]


class NaturalLangItemType:
    id: int
    natural_lang: str
    level: str


CvNaturalLangType = tuple[BlockNameType, NaturalLangItemType]
