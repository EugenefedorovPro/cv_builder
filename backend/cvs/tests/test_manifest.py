import json

import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse

from ..models.models import Experience


class ManifestTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.builder = TestBuilderSuper().create_user().create_lang().create_manifest()

    def setUp(self):
        logged_in = self.client.login(username = self.builder.username, password = self.builder.password)
        self.assertTrue(logged_in)

    def test_manifest(self):
        url = reverse("cvs:manifest")
        response = self.client.get(url)
        actual = json.loads(response.content.decode())
        expected = {
            'id': 1,
            'manifest_text': 'Backend Software Engineer with a strong understanding of '
                             'frontend development, an analytical background, and '
                             'hands-on experience in Neural Network development.'

            }

        self.assertEqual(actual, expected)
