import json

import ipdb
from cvs.tests.data import header_user_super
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from pprint import pprint

from .populate_test_db import TestBuilderSuper

User = get_user_model()


class HeaderTest(TestCase):

    def setUp(self):
        self.builder = (
            TestBuilderSuper()
            .create_user()
            .create_lang()
            .create_occupation()
            .create_block_names()
            .create_photo()
            .create_header()
        )
        logged_in = self.client.login(
            username=self.builder.username,
            password=self.builder.password,
        )
        self.assertTrue(logged_in)

    def get_actual_header(self):
        url = reverse("cvs:header")
        response = self.client.get(url + "?lang=eng")
        actual_header = json.loads(response.content.decode())
        return actual_header

    def test_get(self):
        expected_header = {
            'block_names': {
                'github_title': 'github',
                'linkedin_title': 'linkedin',
                'country_title': 'Country: ',
                'city_title': 'City: ',
                'district_title': 'District: '
            },
            'header': {
                'id': 1,
                'first_name': 'Eugene',
                'second_name': 'Proskulikov',
                'phone': '+38-(096)-464-3910',
                'email': 'eugene.proskulikov@gmail.com',
                'linkedin': 'https://www.linkedin.com/in/eugene-proskulikov-168050a4/',
                'github': 'https://github.com/EugenefedorovPro/',
                'country': 'Ukraine',
                'city': 'Kyiv',
                'district': 'Left Bank'
            }
        }

        expected_photo = {
            'photo_url': '/media/photos/test_image'
        }

        actual_header = self.get_actual_header()
        actual_photo = actual_header["header"].pop("photo")
        pprint(f"actual_header = {actual_header}")
        pprint(f"actual_photo = {actual_photo}")

        self.assertEqual(actual_header, expected_header)
        self.assertIn(expected_photo["photo_url"], actual_photo["photo_url"])
