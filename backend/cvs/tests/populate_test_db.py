import ipdb
from pathlib import Path
from django.core.files import File
from django.utils.choices import BlankChoiceIterator

from cvs.models.models import (Header,
                               HardSkill,
                               Photos,
                               LanguageChoice,
                               BlockNames,
                               Manifest,
                               Project,
                               SoftSkill,
                               Education,
                               Experience,
                               Interest,

                               )
from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from abc import (ABC,
                 abstractmethod,
                 )
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from cvs.tests.data import (BLOCK_NAME_ENG,
                            PHOTO,
                            USER_SUPER,
                            USER_SIMPLE,
                            HEADER_USER_SUPER,
                            HEADER_USER_SIMPLE,
                            HARD_SKILLS_ENG,
                            MANIFEST_ENG,
                            PROJECTS_ENG,
                            ProjectTuple,
                            HardSkillTuple,
                            SOFT_SKILLS_ENG,
                            SoftSkillTuple,
                            EducationTuple,
                            EDUCATION_ENG,
                            EXPERIENCE_ENG,
                            ExperienceTuple,
                            InterestTuple,
                            INTERESTS_ENG,


                            )

User = get_user_model()


class CvBlockInterface(ABC):
    @abstractmethod
    def create_block(self):
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
                username = self.username,
                password = self.password,
                )
        else:
            return User.objects.create_user(
                username = self.username,
                password = self.password,
                is_staff = self.is_staff,
                )


class UserSuper(UserFactory):
    def __init__(self):
        super().__init__(
            **USER_SUPER,
            )


class UserSimple(UserFactory):
    def __init__(self):
        super().__init__(**USER_SIMPLE)


class BlockNamesFactory(CvBlockInterface):
    def __init__(self, lang: LanguageChoice, data: dict[str, str]):
        self.lang = lang
        self.data = data

    def create_block(self):
        return BlockNames.objects.create(**self.data, lang = self.lang)


class BlockNamesEng(BlockNamesFactory):
    data = BLOCK_NAME_ENG.copy()

    def __init__(self, lang: LanguageChoice):
        self.lang = lang
        super().__init__(self.lang, self.data)


class PhotoFactory(CvBlockInterface):
    def __init__(self, **photo):
        self.user = photo["user"]
        self.description = photo["description"]
        self.name = photo["name"]
        self.width = photo["width"]
        self.height = photo["height"]
        self.color = photo["color"]
        self.mode = photo["mode"]
        self.format = photo["format"]

    def create_block(self):
        image = Image.new(self.mode, (self.width, self.height), color = self.color)
        buffer = BytesIO()
        image.save(buffer, format = self.format)
        buffer.seek(0)
        image_file = SimpleUploadedFile(self.name, buffer.read(), content_type = f"image/{self.format.lower()}")
        photo = Photos.objects.create(
            photo_url = image_file,
            description = self.description,
            user = self.user,
            )
        return photo


class PhotoSuper(PhotoFactory):
    def __init__(self, user: User):
        PHOTO["user"] = user
        super().__init__(**PHOTO)


class HeaderFactory(CvBlockInterface):
    def __init__(self, **data):
        self.user = data["user"]
        self.lang = data["lang"]
        self.photo = data["photo"]
        self.first_name = data["first_name"]
        self.second_name = data["second_name"]
        self.phone = data["phone"]
        self.email = data["email"]
        self.linkedin = data["linkedin"]
        self.github = data["github"]
        self.country = data["country"]
        self.city = data["city"]
        self.district = data["district"]

    def create_block(self):
        return Header.objects.create(
            first_name = self.first_name,
            second_name = self.second_name,
            phone = self.phone,
            email = self.email,
            linkedin = self.linkedin,
            github = self.github,
            country = self.country,
            city = self.city,
            district = self.district,
            photo = self.photo,
            lang = self.lang,
            user = self.user,

            ),


class HeaderUserSuper(HeaderFactory):
    data = HEADER_USER_SUPER.copy()

    def __init__(self, user: User, lang: LanguageChoice, photo: Photos):
        self.data["user"] = user
        self.data["lang"] = lang
        self.data["photo"] = photo
        super().__init__(**self.data)


class HeaderUserSimple(HeaderFactory):
    data = HEADER_USER_SIMPLE.copy()

    def __init__(self, user: User, lang: LanguageChoice, photo: Photos):
        self.data["user"] = user
        self.data["lang"] = lang
        self.data["photo"] = photo
        super().__init__(**self.data)


class HardSkillsFactory(CvBlockInterface):
    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice, data: list[HardSkillTuple]):
        self.block_names = block_names
        self.user = user
        self.lang = lang
        self.data = data

    def create_block(self) -> list[HardSkill]:
        hard_skills: list[HardSkill] = []
        for hard_skill in self.data:
            hard_skills.append(
                HardSkill(
                    id = hard_skill.id,
                    block_name = self.block_names,
                    category = hard_skill.category,
                    hard_skill_text = hard_skill.hard_skill_text,
                    user = self.user,
                    lang = self.lang,
                    )
                )
        return HardSkill.objects.bulk_create(hard_skills)


class HardSkillEng(HardSkillsFactory):

    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice):
        super().__init__(block_names, user, lang, HARD_SKILLS_ENG)


class LangFactory(CvBlockInterface):
    def __init__(self, lang: str):
        self.lang = lang

    def create_block(self):
        return LanguageChoice.objects.create(lang = self.lang)


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
    def __init__(self, user: User, lang: LanguageChoice, manifest_text: str):
        self.user = user
        self.lang = lang
        self.manifest_text = manifest_text

    def create_block(self):
        return Manifest.objects.create(
            user = self.user,
            lang = self.lang,
            manifest_text = self.manifest_text

            )


class ManifestEng(ManifestFactory):
    def __init__(self, user: User, lang: LanguageChoice):
        super().__init__(user, lang, MANIFEST_ENG)


class ProjectsFactory(CvBlockInterface):
    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice, data: dict[int, ProjectTuple]):
        self.block_names = block_names
        self.user = user
        self.lang = lang
        self.data = data

    def create_block(self):
        projects: list[Project] = []
        for id_num, project in self.data.items():
            projects.append(
                Project(
                    id = id_num,
                    block_name = self.block_names,
                    user = self.user,
                    lang = self.lang,
                    project_name = project.project_name,
                    project_text = project.project_text,
                    web_url = project.web_url,
                    git_url = project.git_url,
                    )
                )
        return Project.objects.bulk_create(projects)


class ProjectsEng(ProjectsFactory):
    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice):
        super().__init__(block_names, user, lang, PROJECTS_ENG)


class ExperienceFactory(CvBlockInterface):
    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice, data: list[ExperienceTuple]):
        self.block_names = block_names
        self.user = user
        self.lang = lang
        self.data = data

    def create_block(self):
        experience_items: list[Experience] = []
        for item in self.data:
            experience_items.append(
                Experience(
                    id = item.id,
                    block_name = self.block_names,
                    user = self.user,
                    lang = self.lang,
                    company = item.company,
                    position = item.position,
                    start_date = item.start_date,
                    end_date = item.end_date,
                    achievements = item.achievements,
                    )
                )
        return Experience.objects.bulk_create(experience_items)


class ExperienceEng(ExperienceFactory):
    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice):
        super().__init__(block_names, user, lang, EXPERIENCE_ENG)


class SoftSkillsFactory(CvBlockInterface):
    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice, data: list[SoftSkillTuple]):
        self.block_names = block_names
        self.user = user
        self.lang = lang
        self.data = data

    def create_block(self):
        soft_skills: list[SoftSkill] = []
        for item in self.data:
            soft_skills.append(
                SoftSkill(
                    id = item.id,
                    user = self.user,
                    lang = self.lang,
                    block_name = self.block_names,
                    soft_skill_text = item.soft_skill_text,

                    )
                )
        return SoftSkill.objects.bulk_create(soft_skills)


class SoftSkillsEng(SoftSkillsFactory):
    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice):
        super().__init__(block_names, user, lang, SOFT_SKILLS_ENG)


class EducationFactory(CvBlockInterface):
    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice, data: list[EducationTuple]):
        self.block_names = block_names
        self.user = user
        self.lang = lang
        self.data = data

    def create_block(self):
        education_items: list[Education] = []
        for item in self.data:
            education_items.append(
                Education(
                    id = item.id,
                    block_name = self.block_names,
                    institution = item.institution,
                    start_date = item.start_date,
                    end_date = item.end_date,
                    degree_title = item.degree_title,
                    user = self.user,
                    lang = self.lang,

                    )
                )
        return Education.objects.bulk_create(education_items)


class EducationEng(EducationFactory):
    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice):
        super().__init__(block_names, user, lang, EDUCATION_ENG)


class InterestFactory(CvBlockInterface):
    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice, data: list[InterestTuple]):
        self.block_names = block_names
        self.user = user
        self.lang = lang
        self.data = data

    def create_block(self):
        interest_items: list[Interest] = []
        for item in self.data:
            interest_items.append(
                Interest(
                    id = item.id,
                    block_name = self.block_names,
                    interest_text = item.interest_text,
                    user = self.user,
                    lang = self.lang,

                    )
                )
        return Interest.objects.bulk_create(interest_items)


class InterestEng(InterestFactory):
    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice):
        super().__init__(block_names, user, lang, INTERESTS_ENG)


class TestBuilderSuper:
    def __init__(self):
        self.user: User = None
        self.username: str = ""
        self.password: str = ""
        self.lang: LanguageChoice | None = None
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

    def create_user(self) -> User:
        inst = UserSuper()

        self.username = inst.username
        self.password = inst.password
        self.user = inst.create_block()
        return self

    def create_lang(self):
        self.lang = EngLang().create_block()
        return self

    def create_block_names(self):
        self.block_names = BlockNamesEng(self.lang).create_block()
        return self


    def create_photo(self) -> Photos:
        self.photo = PhotoSuper(user = self.user).create_block()
        return self

    def create_header(self) -> Header:
        self.header = HeaderUserSuper(user = self.user, lang = self.lang, photo = self.photo).create_block()
        return self

    def create_hard_skills(self) -> list[HardSkill]:
        self.hard_skills = HardSkillEng(self.block_names, self.user, self.lang).create_block()
        return self

    def create_manifest(self):
        self.manifest = ManifestEng(user = self.user, lang = self.lang).create_block()
        return self

    def create_projects(self):
        self.projects = ProjectsEng(self.block_names, self.user, self.lang).create_block()
        return self

    def create_experience(self):
        self.experience = ExperienceEng(self.block_names, self.user, self.lang).create_block()
        return self

    def create_soft_skills(self):
        self.soft_skills = SoftSkillsEng(self.block_names, self.user, self.lang).create_block()
        return self

    def create_education(self):
        self.education = EducationEng(self.block_names, self.user, self.lang).create_block()
        return self

    def create_interest(self):
        self.interest = InterestEng(self.block_names, self.user, self.lang).create_block()
        return self


class EngCvBuilder(TestBuilderSuper):
    def create_user(self):
        self.user = User.objects.create_superuser(
            pk = 1,
            username = "admin",
            password = "sql_1980",
            )
        return self

    def create_photo(self):
        file_name = "quattr.jpg"
        url = Path(__file__).parent.parent / f"management/commands/{file_name}"
        with open(url, "rb") as f:
            self.photo = Photos.objects.create(
                pk = 1,
                user = self.user,
                description = "quattr_photo_eugene_pro",
                )
            self.photo.photo_url.save(file_name, File(f))
        return self
