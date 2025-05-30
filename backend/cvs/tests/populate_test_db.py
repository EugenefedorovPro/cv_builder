from cvs.models.models import Header
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

User = get_user_model()


class PrepareTestData(TestCase):
    def setUp(self):
        self.user_super_username = "user_super"
        self.user_super_password = "user_super_password_1234"
        self.user_simple_username = "user_simple"
        self.user_simple_password = "user_simple_password_1234"
        self.user_super = None
        self.user_simple = None

        self.create_users()
        self.populate_headers()


    def create_users(self):
        self.user_super = User.objects.create_superuser(
            username = self.user_super_username,
            password = self.user_super_password,
            )
        self.user_simple = User.objects.create_user(
            username = self.user_simple_username,
            password = self.user_simple_password,
            is_staff = True,
            )

        header_content_type = ContentType.objects.get_for_model(Header)
        view_header_perm = Permission.objects.get(codename = "view_header", content_type = header_content_type)
        self.user_simple.user_permissions.add(
            view_header_perm,
            )


    def populate_headers(self):
        headers = [
            Header(
                first_name = "user_super_first_name",
                second_name = "user_super_second_name",
                phone = "+1234567890",
                email = "user_super@gmail.com",
                linkedin = "https://www.linkedin.com/in/user_super",
                github = "usersuper.github.com",
                country = "Superland",
                city = "Supercity",
                district = "Superdistrict",
                user = self.user_super,
                ),
            Header(
                first_name = "user_simple_first_name",
                second_name = "user_simple_second_name",
                phone = "+0987654321",
                email = "simple_user@gmail.com",
                linkedin = "https://www.linkedin.com/in/user_simple",
                github = "usersimple.github.com",
                country = "Simpleland",
                city = "Simplecity",
                district = "Simpledistrict",
                user = self.user_simple,
                )
            ]
        return Header.objects.bulk_create(headers)
