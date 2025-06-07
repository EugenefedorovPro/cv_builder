from typing import TypedDict
from datetime import datetime
from collections import namedtuple

DATE_FORMATTER = "%Y-%m-%d"

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

class BlockNameType(TypedDict):
    block_name: str


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
