from typing import TypedDict
from datetime import datetime

DATE_FORMATTER = "%Y-%m-%d"


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
