import json
import ipdb
from django.test import TestCase
from cvs.models.models import Header
from .populate_test_db import HeaderUserSuper
from django.shortcuts import reverse


class HeaderTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.header = HeaderUserSuper()

    def setUp(self):
        logged_in = self.client.login(
            username = self.header.user_super_class.username,
            password = self.header.user_super_class.password,
            )
        self.assertTrue(logged_in)

    def test_get(self):
        url = reverse("cvs:header")
        response = self.client.get(url)
        actual_header= json.loads(response.content.decode())
        expected_header = {
            'city': 'Supercity',
            'country': 'Superland',
            'district': 'Superdistrict',
            'email': 'user_super@gmail.com',
            'first_name': 'user_super_first_name',
            'github': 'https://github.com/user_super',
            'id': 1,
            'linkedin': 'https://www.linkedin.com/in/user_super',
            'phone': '+1234567890',
            'photo': None,
            'second_name': 'user_super_second_name'
            }
        self.assertEqual(expected_header, actual_header)
