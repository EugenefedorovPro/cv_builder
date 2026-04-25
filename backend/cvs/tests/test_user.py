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


class TestSignUp(TestCase):

    def setUp(self):
        self.builder = TestBuilderSuper().create_user()
        logged_in = self.client.login(
            username=self.builder.username,
            password=self.builder.password,
        )
        self.assertTrue(logged_in)

    # @skip("")
    def test_signup(self):
        url = reverse("cvs:signup")
        data: CustomUserType = {
            "username": "test_username",
            "email": "test@gmail.com",
            "password": "Test_pass_12345",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        new_user = CustomUser.objects.filter(username="test_username").first()
        self.assertEqual(new_user.email, data["email"])
        self.assertNotEqual(new_user.password, data["password"])

    # @skip("")
    def test_login(self):
        logged_in = self.client.logout()
        self.assertFalse(logged_in)

        url = reverse("cvs:login")
        data = {
                "username": self.builder.username,
                "password": self.builder.password,
                }
        response = self.client.post(url, data=data)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout(self):
        url = reverse("cvs:logout")
        response = self.client.post(url)
        self.assertFalse(response.wsgi_request.user.is_authenticated)






