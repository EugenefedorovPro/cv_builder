from pathlib import Path

from django.contrib.auth import get_user_model
from django.core.files import File

from cvs.models.models import Photos
from cvs.tests.populate_test_db import TestBuilderSuper

User = get_user_model()


class EngCvBuilder(TestBuilderSuper):
    def create_user(self):
        self.user = User.objects.create_superuser(
            pk=1,
            username="admin",
            password="sql_1980",
            email="eugene.proskulikov@gmail.com",
        )
        return self

    def create_photo(self):
        file_name = "quattr.jpg"
        url = Path(__file__).parent / f"{file_name}"
        with open(url, "rb") as f:
            self.photo, _ = Photos.objects.get_or_create(
                pk=1,
                uuid_url=self.uuid_url,
                description="quattr_photo_eugene_pro",
            )
            self.photo.photo_url.save(file_name, File(f))
        return self
