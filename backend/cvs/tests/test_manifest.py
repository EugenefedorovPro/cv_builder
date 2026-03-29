import json
from pprint import pprint
import ipdb
from cvs.models.models import BlockNames
from cvs.tests.data import MANIFEST_ENG
from django.shortcuts import reverse
from django.test import TestCase

from .populate_test_db import TestBuilderSuper

expected = {
    "block_names": {"manifest_name": "Manifest"},
    "manifest": {
        "id": 1,
        "manifest_text": "Backend Software Engineer with a strong grasp "
        "of frontend development, a solid analytical "
        "background, and practical experience in neural "
        "network development",
    },
}


class ManifestTest(TestCase):
    def setUp(self):
        self.builder = (
            TestBuilderSuper()
            .create_user()
            .create_lang()
            .create_occupation()
            .create_block_names()
            .create_manifest()
        )
        logged_in = self.client.login(
            username=self.builder.username, password=self.builder.password
        )
        self.assertTrue(logged_in)

    def test_manifest(self):
        url = reverse("cvs:manifest")
        response = self.client.get(url + "?lang=eng")
        actual = json.loads(response.content.decode())
        pprint(f"manifest_response = {actual}")
        self.assertEqual(actual, expected)
