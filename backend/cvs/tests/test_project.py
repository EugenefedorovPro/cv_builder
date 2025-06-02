import json

import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse
from cvs.tests.data import MANIFEST_ENG


class ProjectTest(TestCase):
    def setUp(self):
        self.builder = TestBuilderSuper().create_user().create_lang().create_block_names().create_manifest()
        logged_in = self.client.login(username = self.builder.username, password = self.builder.password)
        self.assertTrue(logged_in)


    def test_project(self):
        url = reverse("cvs:project")
        response = self.client.get(url)
        actual = json.loads(response.content.decode())
        expected = [
            {
                'block_name': 'Manifest'
                },
            {
                'id': 1,
                'manifest_text': MANIFEST_ENG,
                }
            ]

        self.assertEqual(actual, expected)
