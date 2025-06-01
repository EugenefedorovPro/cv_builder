import json
import ipdb
from django.test import TestCase
from cvs.models.models import Header
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse


class HeaderTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.builder = TestBuilderSuper().create_user().create_photo().create_header()


    def setUp(self):
        logged_in = self.client.login(
            username = self.builder.username,
            password = self.builder.password,
            )
        self.assertTrue(logged_in)

    def test_get(self):
        url = reverse("cvs:header")
        response = self.client.get(url)
        actual_header = json.loads(response.content.decode())
        actual_photo = actual_header.pop("photo")
        expected_header = {
            'city': 'Kyiv',
            'country': 'Ukraine',
            'district': 'Left Bank',
            'email': 'eugene.proskulikov@gmail.com',
            'first_name': 'Eugene',
            'github': 'https://github.com/EugenefedorovPro/',
            'id': 1,
            'linkedin': 'https://www.linkedin.com/in/eugene-proskulikov-168050a4/',
            'phone': '+38-(096)-464-3910',
            'second_name': 'Proskulikov',

            }
        expected_photo = {
            'photo': {
                'photo_url': '/media/photos/'
                }
            }
        self.assertEqual(expected_header, actual_header)
        self.assertIn(expected_photo["photo"]["photo_url"], actual_photo["photo_url"])
