import ipdb
from django.utils.choices import BlankChoiceIterator

from cvs.models.models import (Header,
                               HardSkill,
                               Photos,
                               LanguageChoice,
                               BlockNames,
                               Manifest,

                               )
from django.contrib.auth import get_user_model
from abc import (ABC,
                 abstractmethod,
                 )
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()


class CvBlockInterface(ABC):
    @abstractmethod
    def create_block(self):
        pass


class UserFactory(CvBlockInterface):
    def __init__(self, username: str, password: str, is_superuser: bool, is_staff: bool = True):
        self.username = username
        self.password = password
        self.is_superuser = is_superuser
        self.is_staff = is_staff

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
            username = "user_super",
            password = "user_super_password_1234",
            is_superuser = True,

            )


class UserSimple(UserFactory):
    def __init__(self):
        super().__init__(
            username = "user_simple",
            password = "user_simple_password_1234",
            is_superuser = False,

            )


class BlockNamesFactory(CvBlockInterface):
    def __init__(self, data):
        self.data = data

    def create_block(self):
        return BlockNames.objects.create(**self.data)


class BlockNamesEng(BlockNamesFactory):
    data: dict[str, str] = {
        "header_name": "Header",
        "hard_skills_name": "Hard Skills",
        "manifest_name": "Manifest",
        "projects_name": "Projects",
        "experience_name": "Experience",
        "soft_skills_name": "Soft Skills",
        "education_name": "Education",
        "hobby_name": "Hobby",
        "cases_name": "Cases",
        "why_me_name": "Why me?",
        }

    def __init__(self, lang: LanguageChoice):
        self.lang = lang
        self.data.setdefault("lang_id", lang.pk)
        super().__init__(self.data)


class PhotoFactory(CvBlockInterface):
    def __init__(self, user: User, description: str, name: str, width: int, height: int, color: str, mode: str = "RGB", format: str = "JPEG"):
        self.user = user
        self.description = description
        self.name = name
        self.width = width
        self.height = height
        self.color = color
        self.mode = mode
        self.format = format

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
        super().__init__(
            user = user,
            description = "test_photo_super",
            name = "test_image.jpg",
            width = 150,
            height = 200,
            color = "Red",
            mode = "RGB",
            format = "JPEG",
            )


class HeaderFactory(CvBlockInterface):
    def __init__(self, user: User, lang: LanguageChoice, photo: Photos, first_name: str, second_name: str, phone: str, email: str,
                 linkedin: str, github: str, country: str, city: str, district: str):
        self.user = user
        self.lang = lang
        self.photo = photo
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self.email = email
        self.linkedin = linkedin
        self.github = github
        self.country = country
        self.city = city
        self.district = district

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
    def __init__(self, user: User, lang: LanguageChoice, photo: Photos):
        super().__init__(
            photo = photo,
            lang = lang,
            user = user,
            first_name = "Eugene",
            second_name = "Proskulikov",
            phone = "+38-(096)-464-3910",
            email = "eugene.proskulikov@gmail.com",
            linkedin = "https://www.linkedin.com/in/eugene-proskulikov-168050a4/",
            github = "https://github.com/EugenefedorovPro/",
            country = "Ukraine",
            city = "Kyiv",
            district = "Left Bank"

            )


class HeaderUserSimple(HeaderFactory):
    def __init__(self, user: User, lang: LanguageChoice, photo: Photos):
        super().__init__(
            user = user,
            lang = lang,
            photo = photo,
            first_name = "user_simple_first_name",
            second_name = "user_simple_second_name",
            phone = "+0987654321",
            email = "simple_user@gmail.com",
            linkedin = "https://www.linkedin.com/in/user_simple",
            github = "usersimple.github.com",
            country = "Simpleland",
            city = "Simplecity",
            district = "Simpledistrict",
            )


class HardSkillsFactory(CvBlockInterface):
    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice, data: dict[str, str]):
        self.block_names = block_names
        self.user = user
        self.lang = lang
        self.data = data

    def create_block(self) -> list[HardSkill]:
        hard_skills: list[HardSkill] = []
        for category, text in self.data.items():
            hard_skills.append(
                HardSkill(
                    block_name = self.block_names,
                    category = category,
                    hard_skill_text = text,
                    user = self.user,
                    lang = self.lang,
                    )
                )
        return HardSkill.objects.bulk_create(hard_skills)


class HardSkillUserSuper(HardSkillsFactory):
    data = {
        'Backend': 'Python, Django, Django Rest Api',
        'Frontend': 'React, html, css, bootstrap, JS, JQuery',
        'NN and DataScience': 'Keras + TensorFlow  (GRU models), numpy, pandas, unstructured texts and media field analysis with LooqMe, Semantrum, R',
        'Databases': 'sqlite, MySql, Postgres',
        'DevOps': 'docker, git, nginx, gunicorn, daphne, Linux, CI/CD, SSL, servers setup: VPS, RaspberryPI ',
        'Backend Utilities': 'Redis, Celery (worker, beat), WebSocket',
        'Network Engineering': 'VPN (OpenVpn, Wireguard), eoip, Graphana + Prometeus, firewalls, vlans, networks building',
        'IDE': 'vim, PyCharm',
        }

    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice):
        super().__init__(
            block_names = block_names,
            user = user,
            lang = lang,
            data = self.data,

            )


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
    data = (
        "Backend Software Engineer with a strong understanding of frontend development, "
        "an analytical background, and hands-on experience in Neural Network development.")

    def __init__(self, user: User, lang: LanguageChoice):
        super().__init__(user, lang, self.data)


class TestBuilderSuper:
    def __init__(self):
        self.user: User = None
        self.username: str = ""
        self.password: str = ""
        self.lang: LanguageChoice | None = None
        self.block_names: BlockNames | None = None
        self.photo: Photos | None = None
        self.header: Header | None = None
        self.hard_skills: list[HardSkill] | None = []
        self.manifest: Manifest | None = None

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
        self.hard_skills = HardSkillUserSuper(self.block_names, self.user, self.lang).create_block()
        return self

    def create_manifest(self):
        ManifestEng(user = self.user, lang = self.lang).create_block()
        return self
