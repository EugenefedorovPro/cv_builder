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
from cvs.tests.data import BLOCK_NAME_ENG, PHOTO, USER_SUPER, USER_SIMPLE, HEADER_USER_SUPER, HEADER_USER_SIMPLE, HARD_SKILLS_SUPER

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
    def __init__(self, data):
        self.data = data

    def create_block(self):
        return BlockNames.objects.create(**self.data)


class BlockNamesEng(BlockNamesFactory):
    def __init__(self, lang: LanguageChoice):
        self.lang = lang
        BLOCK_NAME_ENG.setdefault("lang_id", lang.pk)
        super().__init__(BLOCK_NAME_ENG)


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
    def __init__(self, user: User, lang: LanguageChoice, photo: Photos):
        HEADER_USER_SUPER["user"] = user
        HEADER_USER_SUPER["lang"] = lang
        HEADER_USER_SUPER["photo"] = photo
        super().__init__(**HEADER_USER_SUPER)


class HeaderUserSimple(HeaderFactory):
    def __init__(self, user: User, lang: LanguageChoice, photo: Photos):
        HEADER_USER_SIMPLE["user"] = user
        HEADER_USER_SIMPLE["lang"] = lang
        HEADER_USER_SIMPLE["photo"] = photo
        super().__init__(**HEADER_USER_SIMPLE)


class HardSkillsFactory(CvBlockInterface):
    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice, data):
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

    def __init__(self, block_names: BlockNames, user: User, lang: LanguageChoice):
        super().__init__(block_names, user, lang, HARD_SKILLS_SUPER)


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
        super().__init__(user, lang, ManifestEng)


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
