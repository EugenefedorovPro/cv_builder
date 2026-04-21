from abc import ABC, abstractmethod
from io import BytesIO

import ipdb
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import QuerySet
from PIL import Image

from cvs.models.models import (
    BlockNames,
    Education,
    Experience,
    HardSkill,
    Header,
    Interest,
    LanguageChoice,
    Manifest,
    NaturalLanguage,
    OccupationChoice,
    Photos,
    Project,
    SoftSkill,
    UuidUrl,
)
from cvs.tests.data import (
    BLOCK_NAMES,
    EDUCATION_ENG,
    EXPERIENCE_ENG,
    HARD_SKILLS_ENG,
    HEADERS_ENG,
    INTERESTS_ENG,
    MANIFEST_ENG,
    NATURAL_LANGS_ENG,
    OCCUPATION_ENG,
    PHOTO_ENG,
    PROJECTS_ENG,
    SOFT_SKILLS_ENG,
    USER_SIMPLE,
    USER_SUPER,
    BlockNameTuple,
    EducationTuple,
    ExperienceTuple,
    HardSkillTuple,
    HeaderTuple,
    InterestTuple,
    ManifestTuple,
    NaturalLangTuple,
    OccupationChoiceTuple,
    PhotoTuple,
    ProjectTuple,
    SoftSkillTuple,
)

User = get_user_model()


class CvBlockInterface(ABC):
    @abstractmethod
    def create_block(self) -> User:
        pass


class UserFactory(CvBlockInterface):
    def __init__(self, **data):
        self.username = data["username"]
        self.password = data["password"]
        self.is_superuser = data["is_superuser"]
        self.is_staff = True if not data.get("is_staff", None) else data["is_staff"]

    def create_block(self) -> User:
        if self.is_superuser:
            return User.objects.create_superuser(
                username=self.username,
                password=self.password,
            )
        else:
            return User.objects.create_user(
                username=self.username,
                password=self.password,
                is_staff=self.is_staff,
            )


class UserSuper(UserFactory):
    def __init__(self):
        super().__init__(
            **USER_SUPER,
        )


class UserSimple(UserFactory):
    def __init__(self):
        super().__init__(**USER_SIMPLE)


class OccupationFactory(CvBlockInterface):
    def __init__(self, data: OccupationChoiceTuple):
        self.data = data

    def create_block(self, user: User) -> QuerySet[OccupationChoice]:
        obj, _created = OccupationChoice.objects.get_or_create(
            id=self.data.id,
            occupation=self.data.occupation,
            user=user,
        )
        return obj


class OccupationEng(OccupationFactory):
    def __init__(self):
        super().__init__(OCCUPATION_ENG)


class UuidUrlUniversal(CvBlockInterface):
    def __init__(self, user: User, occupation: OccupationChoice):
        self.user = user
        self.occupation = occupation

    def create_block(self):
        obj, _ = UuidUrl.objects.get_or_create(
            id=1,
            user=self.user,
            occupation=self.occupation,
        )
        return obj


class BlockNamesFactory(CvBlockInterface):
    def __init__(
        self,
        uuid_url: UuidUrl,
        lang: LanguageChoice,
        data: list[BlockNameTuple],
    ):
        self.uuid_url = uuid_url
        self.lang = lang
        self.data = data

    def create_block(self) -> list[BlockNames]:
        blocks: list[BlockNames] = []
        for item in self.data:
            obj, _ = BlockNames.objects.get_or_create(
                **item._asdict(),
                uuid_url=self.uuid_url,
                lang=self.lang,
            )
            blocks.append(obj)
        return blocks


class BlockNamesEng(BlockNamesFactory):

    def __init__(self, uuid_url: UuidUrl, lang: LanguageChoice):
        super().__init__(uuid_url, lang, BLOCK_NAMES)


class PhotoFactory(CvBlockInterface):
    def __init__(
        self,
        uuid_url: UuidUrl,
        data: PhotoTuple,
    ):
        self.uuid_url = uuid_url
        self.data = data

    def create_block(self) -> Photos:
        image = Image.new(
            self.data.mode, (self.data.width, self.data.height), color=self.data.color
        )
        buffer = BytesIO()
        image.save(buffer, format=self.data.format)
        buffer.seek(0)
        image_file = SimpleUploadedFile(
            self.data.name,
            buffer.read(),
            content_type=f"image/{self.data.format.lower()}",
        )
        obj, _created = Photos.objects.get_or_create(
            id=self.data.id,
            photo_url=image_file,
            description=self.data.description,
            uuid_url=self.uuid_url,
        )
        return obj


class PhotoEng(PhotoFactory):
    def __init__(self, uuid_url: UuidUrl):
        self.uuid_url: uuid_url 

        super().__init__(uuid_url, PHOTO_ENG)


class HeaderFactory(CvBlockInterface):
    def __init__(
        self,
        uuid_url: UuidUrl,
        lang: LanguageChoice,
        photo: Photos,
        data: HeaderTuple,
    ):
        self.uuid_url = uuid_url
        self.lang = lang
        self.photo = photo
        self.data = data

    def create_block(self) -> list[Header]:
        headers: list[Header] = []
        for item in self.data:
            obj, _created = Header.objects.get_or_create(
                id=item.id,
                first_name=item.first_name,
                second_name=item.second_name,
                phone=item.phone,
                email=item.email,
                linkedin=item.linkedin,
                github=item.github,
                country=item.country,
                city=item.city,
                district=item.district,
                photo=self.photo,
                lang=self.lang,
                uuid_url=self.uuid_url,
            )
            headers.append(obj)
        return headers


class HeaderEng(HeaderFactory):
    def __init__(
        self,
        uuid_url: UuidUrl,
        lang: LanguageChoice,
        photo: Photos,
    ):
        super().__init__(uuid_url, lang, photo, HEADERS_ENG)


class HardSkillsFactory(CvBlockInterface):
    def __init__(
        self,
        uuid_url: UuidUrl,
        lang: LanguageChoice,
        data: list[HardSkillTuple],
    ):
        self.uuid_url = uuid_url
        self.lang = lang
        self.data = data

    def create_block(self) -> list[HardSkill]:
        hard_skills: list[HardSkill] = []
        for hard_skill in self.data:
            obj, created = HardSkill.objects.get_or_create(
                id=hard_skill.id,
                category=hard_skill.category,
                hard_skill_text=hard_skill.hard_skill_text,
                uuid_url=self.uuid_url,
                lang=self.lang,
            )
            hard_skills.append(obj)
        return hard_skills


class HardSkillEng(HardSkillsFactory):

    def __init__(
        self,
        uuid_url: UuidUrl,
        lang: LanguageChoice,
    ):
        super().__init__(uuid_url, lang, HARD_SKILLS_ENG)


class LangFactory(CvBlockInterface):
    def __init__(self, lang: str):
        self.lang = lang

    def create_block(self, user: User):
        obj, _created = LanguageChoice.objects.get_or_create(lang=self.lang, user=user)
        return obj


class EngLang(LangFactory):
    def __init__(self, lang: str = "eng"):
        super().__init__(lang)


class UkrLang(LangFactory):
    def __init__(self, lang: str = "ukr"):
        super().__init__(lang)


class RusLang(LangFactory):
    def __init__(self, lang: str = "rus"):
        super().__init__(lang)


class ManifestFactory(CvBlockInterface):
    def __init__(
        self,
        uuid_url: UuidUrl,
        lang: LanguageChoice,
        manifest: ManifestTuple,
    ):
        self.uuid_url = uuid_url
        self.lang = lang
        self.manifest = manifest

    def create_block(self) -> Manifest:
        obj, _ = Manifest.objects.get_or_create(
            id=self.manifest.id,
            manifest_text=self.manifest.manifest_text,
            uuid_url=self.uuid_url,
            lang=self.lang,
        )
        return obj


class ManifestEng(ManifestFactory):
    def __init__(self, uuid_url: UuidUrl, lang: LanguageChoice):
        super().__init__(uuid_url, lang, MANIFEST_ENG)


class ProjectsFactory(CvBlockInterface):
    def __init__(
        self,
        uuid_url: UuidUrl,
        lang: LanguageChoice,
        data: dict[int, ProjectTuple],
    ):
        self.uuid_url = uuid_url
        self.lang = lang
        self.data = data

    def create_block(self):
        projects: list[Project] = []
        for id_num, project in self.data.items():
            obj, _created = Project.objects.get_or_create(
                id=id_num,
                uuid_url=self.uuid_url,
                lang=self.lang,
                project_name=project.project_name,
                project_text=project.project_text,
                web_url=project.web_url,
                git_url=project.git_url,
            )
            projects.append(obj)
        return projects


class ProjectsEng(ProjectsFactory):
    def __init__(
        self,
        uuid_url: User,
        lang: LanguageChoice,
    ):
        super().__init__(uuid_url, lang, PROJECTS_ENG)


class ExperienceFactory(CvBlockInterface):
    def __init__(
        self,
        uuid_url: UuidUrl,
        lang: LanguageChoice,
        data: list[ExperienceTuple],
    ):
        self.uuid_url = uuid_url
        self.lang = lang
        self.data = data

    def create_block(self):
        experience_items: list[Experience] = []
        for item in self.data:
            obj, _created = Experience.objects.get_or_create(
                id=item.id,
                uuid_url=self.uuid_url,
                lang=self.lang,
                company=item.company,
                position=item.position,
                start_date=item.start_date,
                end_date=item.end_date,
                achievements=item.achievements,
            )

            experience_items.append(obj)
        return experience_items


class ExperienceEng(ExperienceFactory):
    def __init__(self, uuid_url: UuidUrl, lang: LanguageChoice):
        super().__init__(uuid_url, lang, EXPERIENCE_ENG)


class SoftSkillsFactory(CvBlockInterface):
    def __init__(
        self,
        uuid_url: UuidUrl,
        lang: LanguageChoice,
        data: list[SoftSkillTuple],
    ):
        self.uuid_url = uuid_url
        self.lang = lang
        self.data = data

    def create_block(self):
        soft_skills: list[SoftSkill] = []
        for item in self.data:
            obj, _created = SoftSkill.objects.get_or_create(
                id=item.id,
                uuid_url=self.uuid_url,
                lang=self.lang,
                soft_skill_text=item.soft_skill_text,
            )
            soft_skills.append(obj)
        return soft_skills


class SoftSkillsEng(SoftSkillsFactory):
    def __init__(
        self,
        uuid_url: UuidUrl,
        lang: LanguageChoice,
    ):
        super().__init__(uuid_url, lang, SOFT_SKILLS_ENG)


class EducationFactory(CvBlockInterface):
    def __init__(
        self,
        uuid_url: UuidUrl,
        lang: LanguageChoice,
        data: list[EducationTuple],
    ):
        self.uuid_url = uuid_url
        self.lang = lang
        self.data = data

    def create_block(self):
        education_items: list[Education] = []
        for item in self.data:
            obj, _craeted = Education.objects.get_or_create(
                id=item.id,
                institution=item.institution,
                start_date=item.start_date,
                end_date=item.end_date,
                degree_title=item.degree_title,
                uuid_url=self.uuid_url,
                lang=self.lang,
            )
            education_items.append(obj)
        return education_items


class EducationEng(EducationFactory):
    def __init__(self, uuid_url: UuidUrl, lang: LanguageChoice):
        super().__init__(uuid_url, lang, EDUCATION_ENG)


class InterestFactory(CvBlockInterface):
    def __init__(
        self,
        uuid_url: UuidUrl,
        lang: LanguageChoice,
        data: list[InterestTuple],
    ):
        self.uuid_url = uuid_url
        self.lang = lang
        self.data = data

    def create_block(self):
        interest_items: list[Interest] = []
        for item in self.data:
            obj, _created = Interest.objects.get_or_create(
                id=item.id,
                interest_text=item.interest_text,
                uuid_url=self.uuid_url,
                lang=self.lang,
            )
            interest_items.append(obj)
        return interest_items


class InterestEng(InterestFactory):
    def __init__(self, uuid_url: UuidUrl, lang: LanguageChoice):
        super().__init__(uuid_url, lang, INTERESTS_ENG)


class NaturalLangFactory(CvBlockInterface):
    def __init__(
        self,
        uuid_url: UuidUrl,
        lang: LanguageChoice,
        data: list[NaturalLangTuple],
    ):
        self.uuid_url = uuid_url
        self.lang = lang
        self.data = data

    def create_block(self):
        natural_lang_items: list[NaturalLanguage] = []
        for item in self.data:
            obj, _created = NaturalLanguage.objects.get_or_create(
                id=item.id,
                natural_lang=item.natural_lang,
                level=item.level,
                uuid_url=self.uuid_url,
                lang=self.lang,
            )
            natural_lang_items.append(obj)
        return natural_lang_items


class NaturalLangEng(NaturalLangFactory):
    def __init__(self, uuid_url: UuidUrl, lang: LanguageChoice):
        super().__init__(uuid_url, lang, NATURAL_LANGS_ENG)


class TestBuilderSuper:
    def __init__(self):
        self.user: User = None
        self.username: str = ""
        self.password: str = ""
        self.lang: LanguageChoice | None = None
        self.occupation: OccupationChoice | None = None
        self.uuid_url: UuidUrl | None = None
        self.block_names: BlockNames | None = None
        self.photo: Photos | None = None
        self.header: Header | None = None
        self.hard_skills: list[HardSkill] = []
        self.manifest: Manifest | None = None
        self.projects: list[Project] = []
        self.experience: list[Experience] = []
        self.soft_skills: list[SoftSkill] = []
        self.education: list[Education] = []
        self.interest: list[Interest] = []
        self.natural_lang: list[NaturalLanguage] = []

    def create_user(self) -> User:
        inst = UserSuper()

        self.username = inst.username
        self.password = inst.password
        self.user = inst.create_block()
        return self

    def create_occupation(self):
        self.occupation = OccupationEng().create_block(self.user)
        return self

    def create_uuid_url(self):
        self.uuid_url = UuidUrlUniversal(self.user, self.occupation).create_block()
        return self

    def create_lang(self):
        self.lang = EngLang().create_block(self.user)
        return self

    def create_block_names(self):
        self.block_names = BlockNamesEng(self.uuid_url, self.lang).create_block()
        return self

    def create_photo(self) -> Photos:
        self.photo = PhotoEng(
            uuid_url=self.uuid_url, lang=self.lang
        ).create_block()
        return self

    def create_header(self) -> Header:
        self.header = HeaderEng(
            uuid_url=self.uuid_url, lang=self.lang, photo=self.photo
        ).create_block()
        return self

    def create_manifest(self):
        self.manifest = ManifestEng(
            uuid_url=self.uuid_url, lang=self.lang
        ).create_block()
        return self

    def create_hard_skills(self) -> list[HardSkill]:
        self.hard_skills = HardSkillEng(
            uuid_url=self.uuid_url, lang=self.lang
        ).create_block()
        return self

    def create_projects(self):
        self.projects = ProjectsEng(
            uuid_url=self.uuid_url, lang=self.lang
        ).create_block()
        return self

    def create_experience(self):
        self.experience = ExperienceEng(
            uuid_url=self.uuid_url, lang=self.lang
        ).create_block()
        return self

    def create_soft_skills(self):
        self.soft_skills = SoftSkillsEng(
            uuid_url=self.uuid_url, lang=self.lang
        ).create_block()
        return self

    def create_education(self):
        self.education = EducationEng(
            uuid_url=self.uuid_url, lang=self.lang
        ).create_block()
        return self

    def create_interest(self):
        self.interest = InterestEng(
            uuid_url=self.uuid_url, lang=self.lang
        ).create_block()
        return self

    def create_natural_lang(self):
        self.natural_lang = NaturalLangEng(
            uuid_url=self.uuid_url, lang=self.lang
        ).create_block()
        return self
