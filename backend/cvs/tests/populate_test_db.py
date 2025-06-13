from django.db.models import QuerySet
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
                               NaturalLanguage,
                               OccupationChoice,

                               )
from django.contrib.auth import get_user_model
from abc import (ABC,
                 abstractmethod,
                 )
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from cvs.tests.data import (BLOCK_NAMES,
                            PHOTO_ENG,
                            USER_SUPER,
                            USER_SIMPLE,
                            HEADERS_ENG,
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
                            NaturalLangTuple,
                            NATURAL_LANGS_ENG,
                            OccupationChoiceTuple,
                            OCCUPATION_ENG,
                            HeaderTuple,
                            PhotoTuple,
                            BlockNameTuple,


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


class OccupationFactory(CvBlockInterface):
    def __init__(self, data: OccupationChoiceTuple):
        self.data = data

    def create_block(self) -> QuerySet[OccupationChoice]:
        return OccupationChoice.objects.create(
            id = self.data.id,
            occupation = self.data.occupation,
            )


class OccupationEng(OccupationFactory):
    def __init__(self):
        super().__init__(OCCUPATION_ENG)


class BlockNamesFactory(CvBlockInterface):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, data: BlockNameTuple):
        self.user = user
        self.lang = lang
        self.occupation = occupation
        self.data = data

    def create_block(self) -> QuerySet[BlockNames]:
        blocks: list[BlockNames] = []
        for item in self.data:
            blocks.append(
                BlockNames(
                    id = item.id,
                    photo_name = item.photo_name,
                    header_name = item.header_name,
                    hard_skills_name = item.hard_skills_name,
                    manifest_name = item.manifest_name,
                    projects_name = item.projects_name,
                    experience_name = item.experience_name,
                    soft_skills_name = item.soft_skills_name,
                    education_name = item.education_name,
                    natural_lang_name = item.natural_lang_name,
                    interest_name = item.interest_name,
                    cases_name = item.cases_name,
                    why_me_name = item.why_me_name,
                    feedback_name = item.feedback_name,
                    user = self.user,
                    lang = self.lang,
                    occupation = self.occupation,

                    )
                )
        return BlockNames.objects.bulk_create(blocks)


class BlockNamesEng(BlockNamesFactory):

    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice):
        self.user = user
        self.lang = lang
        self.occupation = occupation

        super().__init__(user, lang, occupation, BLOCK_NAMES)


class PhotoFactory(CvBlockInterface):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, data: PhotoTuple):
        self.user = user
        self.lang = lang
        self.occupation = occupation
        self.data = data

    def create_block(self) -> Photos:
        image = Image.new(self.data.mode, (self.data.width, self.data.height), color = self.data.color)
        buffer = BytesIO()
        image.save(buffer, format = self.data.format)
        buffer.seek(0)
        image_file = SimpleUploadedFile(self.data.name, buffer.read(), content_type = f"image/{self.data.format.lower()}")
        return Photos.objects.create(
            id = self.data.id,
            photo_url = image_file,
            description = self.data.description,
            user = self.user,
            lang = self.lang,
            occupation = self.occupation,
            )


class PhotoEng(PhotoFactory):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice):
        self.user = user
        self.lang = lang
        self.occupation = occupation

        super().__init__(user, lang, occupation, PHOTO_ENG)


class HeaderFactory(CvBlockInterface):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, photo: Photos, data: HeaderTuple):
        self.user = user
        self.lang = lang
        self.occupation = occupation
        self.photo = photo
        self.data = data


    def create_block(self) -> QuerySet[Header]:
        headers: list[Header] = []
        for item in self.data:
            headers.append(
                Header(
                    id = item.id,
                    first_name = item.first_name,
                    second_name = item.second_name,
                    phone = item.phone,
                    email = item.email,
                    linkedin = item.linkedin,
                    github = item.github,
                    country = item.country,
                    city = item.city,
                    district = item.district,
                    photo = self.photo,
                    lang = self.lang,
                    user = self.user,
                    occupation = self.occupation,

                    ),
                )
        return Header.objects.bulk_create(headers)


class HeaderEng(HeaderFactory):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, photo: Photos):
        self.user = user
        self.lang = lang
        self.occupation = occupation
        self.data = photo
        super().__init__(user, lang, occupation, photo, HEADERS_ENG)


class HardSkillsFactory(CvBlockInterface):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, data:
    list[HardSkillTuple]):
        self.user = user
        self.lang = lang
        self.occupation = occupation
        self.data = data

    def create_block(self) -> list[HardSkill]:
        hard_skills: list[HardSkill] = []
        for hard_skill in self.data:
            hard_skills.append(
                HardSkill(
                    id = hard_skill.id,
                    category = hard_skill.category,
                    hard_skill_text = hard_skill.hard_skill_text,
                    user = self.user,
                    lang = self.lang,
                    occupation = self.occupation,

                    )
                )
        return HardSkill.objects.bulk_create(hard_skills)


class HardSkillEng(HardSkillsFactory):

    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, ):
        super().__init__(user, lang, occupation, HARD_SKILLS_ENG)


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
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, manifest_text: str):
        self.user = user
        self.lang = lang
        self.occupation = occupation
        self.manifest_text = manifest_text

    def create_block(self):
        return Manifest.objects.create(
            user = self.user,
            lang = self.lang,
            manifest_text = self.manifest_text,
            occupation = self.occupation,

            )


class ManifestEng(ManifestFactory):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice):
        super().__init__(user, lang, occupation, MANIFEST_ENG)


class ProjectsFactory(CvBlockInterface):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, data:
    dict[int, ProjectTuple]):
        self.user = user
        self.lang = lang
        self.occupation = occupation
        self.data = data

    def create_block(self):
        projects: list[Project] = []
        for id_num, project in self.data.items():
            projects.append(
                Project(
                    id = id_num,
                    user = self.user,
                    lang = self.lang,
                    project_name = project.project_name,
                    project_text = project.project_text,
                    web_url = project.web_url,
                    git_url = project.git_url,
                    occupation = self.occupation,

                    )
                )
        return Project.objects.bulk_create(projects)


class ProjectsEng(ProjectsFactory):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, ):
        super().__init__(user, lang, occupation, PROJECTS_ENG)


class ExperienceFactory(CvBlockInterface):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, data:
    list[ExperienceTuple]):
        self.user = user
        self.lang = lang
        self.occupation = occupation
        self.data = data

    def create_block(self):
        experience_items: list[Experience] = []
        for item in self.data:
            experience_items.append(
                Experience(
                    id = item.id,
                    user = self.user,
                    lang = self.lang,
                    company = item.company,
                    position = item.position,
                    start_date = item.start_date,
                    end_date = item.end_date,
                    achievements = item.achievements,
                    occupation = self.occupation,

                    )
                )
        return Experience.objects.bulk_create(experience_items)


class ExperienceEng(ExperienceFactory):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice):
        super().__init__(user, lang, occupation, EXPERIENCE_ENG)


class SoftSkillsFactory(CvBlockInterface):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, data:
    list[SoftSkillTuple]):
        self.user = user
        self.lang = lang
        self.occupation = occupation
        self.data = data

    def create_block(self):
        soft_skills: list[SoftSkill] = []
        for item in self.data:
            soft_skills.append(
                SoftSkill(
                    id = item.id,
                    user = self.user,
                    lang = self.lang,
                    soft_skill_text = item.soft_skill_text,
                    occupation = self.occupation,

                    )
                )
        return SoftSkill.objects.bulk_create(soft_skills)


class SoftSkillsEng(SoftSkillsFactory):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, ):
        super().__init__(user, lang, occupation, SOFT_SKILLS_ENG)


class EducationFactory(CvBlockInterface):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, data:
    list[EducationTuple]):
        self.user = user
        self.lang = lang
        self.occupation = occupation
        self.data = data

    def create_block(self):
        education_items: list[Education] = []
        for item in self.data:
            education_items.append(
                Education(
                    id = item.id,
                    institution = item.institution,
                    start_date = item.start_date,
                    end_date = item.end_date,
                    degree_title = item.degree_title,
                    user = self.user,
                    lang = self.lang,
                    occupation = self.occupation,

                    )
                )
        return Education.objects.bulk_create(education_items)


class EducationEng(EducationFactory):
    def __init__(self, user: User, occupation: OccupationChoice, lang: LanguageChoice):
        super().__init__(user, lang, occupation, EDUCATION_ENG)


class InterestFactory(CvBlockInterface):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, data:
    list[InterestTuple]):
        self.user = user
        self.lang = lang
        self.occupation = occupation
        self.data = data


    def create_block(self):
        interest_items: list[Interest] = []
        for item in self.data:
            interest_items.append(
                Interest(
                    id = item.id,
                    interest_text = item.interest_text,
                    user = self.user,
                    lang = self.lang,
                    occupation = self.occupation

                    )
                )
        return Interest.objects.bulk_create(interest_items)


class InterestEng(InterestFactory):
    def __init__(self, user: User, occupation: OccupationChoice, lang: LanguageChoice):
        super().__init__(user, lang, occupation, INTERESTS_ENG)


class NaturalLangFactory(CvBlockInterface):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice, data:
    list[NaturalLangTuple]):
        self.user = user
        self.lang = lang
        self.occupation = occupation
        self.data = data

    def create_block(self):
        natural_lang_items: list[NaturalLanguage] = []
        for item in self.data:
            natural_lang_items.append(
                NaturalLanguage(
                    id = item.id,
                    natural_lang = item.natural_lang,
                    level = item.level,
                    user = self.user,
                    lang = self.lang,
                    occupation = self.occupation,
                    )
                )
        return NaturalLanguage.objects.bulk_create(natural_lang_items)


class NaturalLangEng(NaturalLangFactory):
    def __init__(self, user: User, lang: LanguageChoice, occupation: OccupationChoice):
        super().__init__(user, lang, occupation, NATURAL_LANGS_ENG)


class TestBuilderSuper:
    def __init__(self):
        self.user: User = None
        self.username: str = ""
        self.password: str = ""
        self.lang: LanguageChoice | None = None
        self.occupation: OccupationChoice | None = None
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

    def create_lang(self):
        self.lang = EngLang().create_block()
        return self

    def create_occupation(self):
        self.occupation = OccupationEng().create_block()
        return self

    def create_block_names(self):
        self.block_names = BlockNamesEng(self.user, self.lang, self.occupation).create_block()
        return self


    def create_photo(self) -> Photos:
        self.photo = PhotoEng(user = self.user, lang = self.lang, occupation = self.occupation).create_block()
        return self

    def create_header(self) -> Header:
        self.header = HeaderEng(user = self.user, lang = self.lang, occupation = self.occupation, photo = self.photo).create_block()
        return self

    def create_hard_skills(self) -> list[HardSkill]:
        self.hard_skills = HardSkillEng(user = self.user, lang = self.lang, occupation = self.occupation).create_block()
        return self

    def create_manifest(self):
        self.manifest = ManifestEng(user = self.user, lang = self.lang, occupation = self.occupation).create_block()
        return self

    def create_projects(self):
        self.projects = ProjectsEng(user = self.user, lang = self.lang, occupation = self.occupation).create_block()
        return self

    def create_experience(self):
        self.experience = ExperienceEng(user = self.user, lang = self.lang, occupation = self.occupation).create_block()
        return self

    def create_soft_skills(self):
        self.soft_skills = SoftSkillsEng(user = self.user, lang = self.lang, occupation = self.occupation).create_block()
        return self

    def create_education(self):
        self.education = EducationEng(user = self.user, lang = self.lang, occupation = self.occupation).create_block()
        return self

    def create_interest(self):
        self.interest = InterestEng(user = self.user, lang = self.lang, occupation = self.occupation).create_block()
        return self

    def create_natural_lang(self):
        self.natural_lang = NaturalLangEng(user = self.user, lang = self.lang, occupation = self.occupation).create_block()
        return self
