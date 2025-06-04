from typing import TypedDict
from datetime import datetime


class BlockNameType(TypedDict):
    block_name: str


class ProjectItemType(TypedDict):
    id: int
    project_name: str
    project_text: str
    web_url: str
    git_url: str


CvProjectType = tuple[BlockNameType, list[ProjectItemType]]


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
