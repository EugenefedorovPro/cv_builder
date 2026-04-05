import json
from pprint import pprint

import ipdb
from django.test import TestCase
from django.urls import reverse

from .populate_test_db import TestBuilderSuper

expected_user = {
    "user_data": {
        "username": "user_super",
        "first_name": "",
        "last_name": "",
        "email": "",
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

    def test_get_user(self):
        url = reverse("cvs:user")
        response = self.client.get(url)
        actual_user = json.loads(response.content.decode())
        # remove user id as it can change to test several tests at once
        del actual_user["user_data"]["id"]
        self.assertEqual(actual_user, expected_user)
