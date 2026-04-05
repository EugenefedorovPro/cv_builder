import json

from django.shortcuts import reverse
from django.test import TestCase

from .populate_test_db import TestBuilderSuper

expected = {
    "block_names": {"interest_name": "Interests"},
    "interests": [
        {"id": 1, "interest_text": "Philosophy of Mind and AI"},
        {"id": 2, "interest_text": "Avant-garde Art"},
    ],
}


class InterestTest(TestCase):
    def setUp(self):
        self.builder = (
            TestBuilderSuper()
            .create_user()
            .create_lang()
            .create_occupation()
            .create_block_names()
            .create_interest()
        )
        logged_in = self.client.login(
            username=self.builder.username, password=self.builder.password
        )
        self.assertTrue(logged_in)

    def test_interest(self):
        url = reverse("cvs:interest")
        response = self.client.get(url + "?lang=eng")
        actual = json.loads(response.content.decode())
        self.assertEqual(actual, expected)
