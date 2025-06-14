import json

import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse
from cvs.tests.data import MANIFEST_ENG
from cvs.models.models import BlockNames

class ManifestTest(TestCase):
    def setUp(self):
        self.builder = TestBuilderSuper().create_user().create_lang().create_occupation().create_block_names().create_manifest()
        logged_in = self.client.login(username = self.builder.username, password = self.builder.password)
        self.assertTrue(logged_in)


    def test_manifest(self):
        url = reverse("cvs:manifest")
        response = self.client.get(url)
        actual = json.loads(response.content.decode())
        expected = [
            {
                'block_name': BlockNames.objects.all().first().manifest_name
                },
            {
                'id': 1,
                'manifest_text': MANIFEST_ENG,
                }
            ]

        self.assertEqual(actual, expected)
