populate_test_db.py

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
    from cvs.tests.data import (BLOCK_NAME_ENG,
                                PHOTO,
                                USER_SUPER,
                                USER_SIMPLE,
                                HEADER_USER_SUPER,
                                HEADER_USER_SIMPLE,
                                HARD_SKILLS_SUPER,
                                MANIFEST_ENG,
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
            self.data.setdefault("lang_id", lang.pk)
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
            super().__init__(user, lang, MANIFEST_ENG)


    class TestBuilderSuper:
        def __init__(self):
            self.user: User = None
            self.username: str | None = None
            self.password: str | None = None
            self.lang: LanguageChoice | None = None
            self.block_names: BlockNames | None = None
            self.photo: Photos | None = None
            self.header: Header | None = None
            self.hard_skills: list[HardSkill] | None = None
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


test_hard_skills.py
    import json

    import ipdb
    from django.test import TestCase
    from .populate_test_db import TestBuilderSuper
    from django.shortcuts import reverse


    class HardSkillTest(TestCase):
        def setUp(self):
            self.builder = TestBuilderSuper().create_user().create_lang().create_block_names().create_hard_skills()
            logged_in = self.client.login(username = self.builder.username, password = self.builder.password)
            self.assertTrue(logged_in)

        def test_hard_skills(self):
            self.maxDiff = True
            url = reverse("cvs:hard_skills")
            response = self.client.get(url)
            actual_response = json.loads(response.content.decode())
            expected_response = [{
                'block_name': 'Hard Skills'
                },
                [{
                    'category': 'Backend',
                    'hard_skill_text': 'Python, Django, Django Rest Api',
                    'id': 1
                    },
                    {
                        'category': 'Frontend',
                        'hard_skill_text': 'React, html, css, bootstrap, JS, JQuery',
                        'id': 2
                        },
                    {
                        'category': 'NN and DataScience',
                        'hard_skill_text': 'Keras + TensorFlow  (GRU models), numpy, pandas, '
                                           'unstructured texts and media field analysis with '
                                           'LooqMe, Semantrum, R',
                        'id': 3
                        },
                    {
                        'category': 'Databases',
                        'hard_skill_text': 'sqlite, MySql, Postgres',
                        'id': 4
                        },
                    {
                        'category': 'DevOps',
                        'hard_skill_text': 'docker, git, nginx, gunicorn, daphne, Linux, CI/CD, '
                                           'SSL, servers setup: VPS, RaspberryPI ',
                        'id': 5
                        },
                    {
                        'category': 'Backend Utilities',
                        'hard_skill_text': 'Redis, Celery (worker, beat), WebSocket',
                        'id': 6
                        },
                    {
                        'category': 'Network Engineering',
                        'hard_skill_text': 'VPN (OpenVpn, Wireguard), eoip, Graphana + Prometeus, '
                                           'firewalls, vlans, networks building',
                        'id': 7
                        },
                    {
                        'category': 'IDE',
                        'hard_skill_text': 'vim, PyCharm',
                        'id': 8
                        }]]

            self.assertEqual(actual_response, expected_response)

test_header.py

    import json
    import ipdb
    from django.test import TestCase
    from cvs.models.models import Header
    from .populate_test_db import TestBuilderSuper
    from django.shortcuts import reverse
    from cvs.tests.data import HEADER_USER_SUPER
    from django.contrib.auth import get_user_model


    User = get_user_model()


    class HeaderTest(TestCase):
        def setUp(self):
            self.builder = TestBuilderSuper().create_user().create_lang().create_photo().create_header()
            logged_in = self.client.login(
                username = self.builder.username,
                password = self.builder.password,
                )
            self.assertTrue(logged_in)


        def test_get(self):
            url = reverse("cvs:header")
            response = self.client.get(url)
            actual_header = json.loads(response.content.decode())
            actual_photo = actual_header.pop("photo")

            HEADER_USER_SUPER["id"] = 1
            expected_header = HEADER_USER_SUPER
            expected_photo = {
                'photo': {
                    'photo_url': '/media/photos/'
                    }
                }
            self.assertEqual(expected_header, actual_header)
            self.assertIn(expected_photo["photo"]["photo_url"], actual_photo["photo_url"])


test_manifest.py


    import json

    import ipdb
    from django.test import TestCase
    from .populate_test_db import TestBuilderSuper
    from django.shortcuts import reverse
    from cvs.tests.data import MANIFEST_ENG


    class ManifestTest(TestCase):
        def setUp(self):
            self.builder = TestBuilderSuper().create_user().create_lang().create_block_names().create_manifest()
            print("\nmanifest\n")
            print(f"lang pk {self.builder.lang.pk}")
            print(f"block_names lang pk = {self.builder.block_names.pk}")
            logged_in = self.client.login(username = self.builder.username, password = self.builder.password)
            self.assertTrue(logged_in)


        def test_manifest(self):
            url = reverse("cvs:manifest")
            response = self.client.get(url)
            actual = json.loads(response.content.decode())
            expected = [
                {
                    'block_name': 'Manifest'
                    },
                {
                    'id': 1,
                    'manifest_text': MANIFEST_ENG,
                    }
                ]

            self.assertEqual(actual, expected)


when I run test_manifest alone. It works fine.
When I run all tests I have the error:
eugene@eugene-zenbook:~/Documents/cv_builder$ docker compose exec django_app python manage.py test cvs.tests
Found 3 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
manifest

lang pk 3
block_names lang pk = 2
.E
======================================================================
ERROR: test_manifest (cvs.tests.test_manifest.ManifestTest.test_manifest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/utils.py", line 103, in _execute
    return self.cursor.execute(sql)
           ^^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.ForeignKeyViolation: insert or update on table "cvs_blocknames" violates foreign key constraint "cvs_blocknames_lang_id_7b639627_fk_language_choice_id"
DETAIL:  Key (lang_id)=(1) is not present in table "language_choice".


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/postgresql/base.py", line 482, in check_constraints
    cursor.execute("SET CONSTRAINTS ALL IMMEDIATE")
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/utils.py", line 79, in execute
    return self._execute_with_wrappers(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/utils.py", line 92, in _execute_with_wrappers
    return executor(sql, params, many, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
  File "/usr/local/lib/python3.12/site-packages/django/db/utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/utils.py", line 103, in _execute
    return self.cursor.execute(sql)
           ^^^^^^^^^^^^^^^^^^^^^^^^
django.db.utils.IntegrityError: insert or update on table "cvs_blocknames" violates foreign key constraint "cvs_blocknames_lang_id_7b639627_fk_language_choice_id"
DETAIL:  Key (lang_id)=(1) is not present in table "language_choice".


----------------------------------------------------------------------
Ran 3 tests in 1.354s

FAILED (errors=1)
Destroying test database for alias 'default'...

eugene@eugene-zenbook:~/Documents/cv_builder$ 
eugene@eugene-zenbook:~/Documents/cv_builder$ docker compose exec django_app python manage.py test cvs.tests
Found 3 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
manifest

lang pk 3
block_names lang pk = 2
.E
======================================================================
ERROR: test_manifest (cvs.tests.test_manifest.ManifestTest.test_manifest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/utils.py", line 103, in _execute
    return self.cursor.execute(sql)
           ^^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.ForeignKeyViolation: insert or update on table "cvs_blocknames" violates foreign key constraint "cvs_blocknames_lang_id_7b639627_fk_language_choice_id"
DETAIL:  Key (lang_id)=(1) is not present in table "language_choice".


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/postgresql/base.py", line 482, in check_constraints
    cursor.execute("SET CONSTRAINTS ALL IMMEDIATE")
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/utils.py", line 79, in execute
    return self._execute_with_wrappers(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/utils.py", line 92, in _execute_with_wrappers
    return executor(sql, params, many, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
  File "/usr/local/lib/python3.12/site-packages/django/db/utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/utils.py", line 103, in _execute
    return self.cursor.execute(sql)
           ^^^^^^^^^^^^^^^^^^^^^^^^
django.db.utils.IntegrityError: insert or update on table "cvs_blocknames" violates foreign key constraint "cvs_blocknames_lang_id_7b639627_fk_language_choice_id"
DETAIL:  Key (lang_id)=(1) is not present in table "language_choice".


----------------------------------------------------------------------
Ran 3 tests in 1.354s

FAILED (errors=1)
Destroying test database for alias 'default'...

eugene@eugene-zenbook:~/Documents/cv_builder$ 

