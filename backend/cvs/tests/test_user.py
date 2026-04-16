import json
from pprint import pprint
from unittest import skip

import ipdb
from django.test import TestCase
from django.urls import reverse

from cvs.models.models import CustomUser
from cvs.types import CustomUserType

from .populate_test_db import TestBuilderSuper

expected_user_from_db = {
    "user_data": {
        "username": "user_super",
        "email": "",
    }
}
expected_user_placeholders = {
    "user_data": {
        "id": "",
        "username": "Username",
        "email": "Email",
    }
}

expected_user_placeholders_ukr = {
    "user_data": {
        "id": "",
        "username": "Ім'я користувача",
        "email": "Електронна пошта",
    }
}


class TestUser(TestCase):

    def setUp(self):
        self.builder = TestBuilderSuper().create_user()
        logged_in = self.client.login(
            username=self.builder.username,
            password=self.builder.password,
        )
        self.assertTrue(logged_in)

    # @skip("")
    def test_post(self):
        url = reverse("cvs:user")
        data: CustomUserType = {
            "username": "test_username",
            "email": "test@gmail.com",
            "password": "Test_pass_12345",
        }
        response = self.client.post(url + "?lang=eng", data=data)
        self.assertEqual(response.status_code, 201)
        new_user = CustomUser.objects.filter(username="test_username").first()
        self.assertEqual(new_user.email, data["email"])
        self.assertNotEqual(new_user.password, data["password"])

    # @skip("")
    def test_no_lang(self):
        url = reverse("cvs:user", kwargs={"user_id": CustomUser.objects.first().pk})
        response = self.client.get(url)
        actual_user = json.loads(response.content.decode())
        print(f"test_no_lang = {actual_user}")
        print(f"user_id = {CustomUser.objects.first().pk}")
        print(f" - " * 20)
        # remove user id as it can change to test several tests at once
        del actual_user["user_data"]["id"]
        del actual_user["user_data"]["password"]
        self.assertEqual(actual_user, expected_user_from_db)

    # @skip("")
    def test_no_user(self):
        CustomUser.objects.all().delete()

        url = reverse("cvs:user", kwargs={"user_id": 1})
        response = self.client.get(url + "?lang=eng")
        actual_user = json.loads(response.content.decode())
        print(f"test_no_user = {actual_user}")
        print(f"user_id = {CustomUser.objects.first()}")
        print(f" - " * 20)
        # remove user id as it can change to test several tests at once
        self.assertEqual(actual_user, expected_user_placeholders)

    # @skip("")
    def test_get_user(self):
        url = reverse("cvs:user", kwargs={"user_id": CustomUser.objects.first().pk})
        response = self.client.get(url + "?lang=eng")
        actual_user = json.loads(response.content.decode())
        print(f"test_get_user = {actual_user}")
        print(f"user_id = {CustomUser.objects.first().pk}")
        print(f" - " * 20)
        # remove user id as it can change to test several tests at once
        del actual_user["user_data"]["id"]
        del actual_user["user_data"]["password"]
        self.assertEqual(actual_user, expected_user_from_db)

    # @skip("")
    def test_no_user_id(self):
        url = reverse("cvs:user")
        response = self.client.get(url + "?lang=ukr")
        actual_user = json.loads(response.content.decode())
        print(f"test_no_user = {actual_user}")
        print(f"user_id = {CustomUser.objects.first().pk}")
        print(f" - " * 20)
        self.assertEqual(actual_user, expected_user_placeholders_ukr)
