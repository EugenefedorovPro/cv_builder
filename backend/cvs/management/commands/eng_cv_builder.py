from cvs.tests.populate_test_db import TestBuilderSuper
from django.contrib.auth import get_user_model
from cvs.models.models import Photos
from pathlib import Path
from django.core.files import File

User = get_user_model()


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
        url = Path(__file__).parent / f"{file_name}"
        with open(url, "rb") as f:
            self.photo = Photos.objects.create(
                pk = 1,
                user = self.user,
                description = "quattr_photo_eugene_pro",
                )
            self.photo.photo_url.save(file_name, File(f))
        return self
