from cvs.models.models import Header
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

User = get_user_model()


class UserSuper:
    def __init__(self):
        self.username = "user_super"
        self.password = "user_super_password_1234"
        self.user_super = self.create_user_super()

    def create_user_super(self):
        return User.objects.create_superuser(
            username = self.username,
            password = self.password,
            )


class UserSimple:
    def __init__(self):
        self.username = "user_simple"
        self.password = "user_simple_password_1234"
        self.user_simple = self.create_user_simple()

    def create_user_simple(self):
        return User.objects.create_user(
            username = self.username,
            password = self.password,
            is_staff = True,
            )


class HeaderUserSuper:
    def __init__(self):
        self.user_super_class = UserSuper()
        self.header = self.create_header()

    def create_header(self):
        return Header.objects.create(
            first_name = "user_super_first_name",
            second_name = "user_super_second_name",
            phone = "+1234567890",
            email = "user_super@gmail.com",
            linkedin = "https://www.linkedin.com/in/user_super",
            github = "https://github.com/user_super",
            country = "Superland",
            city = "Supercity",
            district = "Superdistrict",
            user = self.user_super_class.user_super,
            ),


class HeaderUserSimple:
    def __init__(self):
        self.user_simple_class = UserSimple().user_simple
        self.header = self.create_header()

    def create_header(self):
        return Header.objects.create(
            first_name = "user_simple_first_name",
            second_name = "user_simple_second_name",
            phone = "+0987654321",
            email = "simple_user@gmail.com",
            linkedin = "https://www.linkedin.com/in/user_simple",
            github = "usersimple.github.com",
            country = "Simpleland",
            city = "Simplecity",
            district = "Simpledistrict",
            user = self.user_simple_class.user_simple,
            )
