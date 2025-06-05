from cv_builder.settings import STATIC_ROOT
from cvs.management.commands.eng_cv_builder import EngCvBuilder
from cvs.models.models import (LanguageChoice,
                               BlockNames,
                               Header, Photos,
                               HardSkill,
                               Manifest,
                               Project,
                               SoftSkill,
                               Education,
                               Interest,
                               )

from django.contrib.auth import get_user_model

User = get_user_model()

class EngCvSettle:

    @staticmethod
    def _remove_data_from_db():
        User.objects.all().delete()
        Photos.objects.all().delete()
        LanguageChoice.objects.all().delete()
        BlockNames.objects.all().delete()
        Header.objects.all().delete()
        HardSkill.objects.all().delete()
        Manifest.objects.all().delete()
        Project.objects.all().delete()
        SoftSkill.objects.all().delete()
        Education.objects.all().delete()
        Interest.objects.all().delete()

    @staticmethod
    def _populate_db():
        (EngCvBuilder()
         .create_user()
         .create_lang()
         .create_photo()
         .create_block_names()
         .create_header()
         .create_hard_skills()
         .create_manifest()
         .create_projects()
         .create_experience()
         .create_soft_skills()
         .create_education()
         .create_interest()
         )

    def settle_cv(self) -> None:
        self._remove_data_from_db()
        self._populate_db()


