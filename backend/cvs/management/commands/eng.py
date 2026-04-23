from django.contrib.auth import get_user_model

from cvs.management.commands.eng_cv_builder import EngCvBuilder
from cvs.models.models import (
    BlockNames,
    Education,
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

User = get_user_model()


class EngCvSettle:

    @staticmethod
    def remove_data_from_db():
        UuidUrl.objects.all().delete()
        User.objects.all().delete()
        LanguageChoice.objects.all().delete()
        OccupationChoice.objects.all().delete()
        Photos.objects.all().delete()
        BlockNames.objects.all().delete()
        Header.objects.all().delete()
        HardSkill.objects.all().delete()
        Manifest.objects.all().delete()
        Project.objects.all().delete()
        SoftSkill.objects.all().delete()
        Education.objects.all().delete()
        Interest.objects.all().delete()
        NaturalLanguage.objects.all().delete()

    @staticmethod
    def populate_db():
        (
            EngCvBuilder()
            .create_user()
            .create_lang()
            .create_occupation()
            .create_uuid_url()
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
            .create_natural_lang()
        )

    def settle_cv(self) -> None:
        self.remove_data_from_db()
        self.populate_db()
