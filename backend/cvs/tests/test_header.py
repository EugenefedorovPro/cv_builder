import json
import ipdb
from django.test import TestCase
from cvs.models.models import Header
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse
from cvs.tests.data import header_user_super
from django.contrib.auth import get_user_model

User = get_user_model()


class HeaderTest(TestCase):
    def setUp(self):
        self.builder = (TestBuilderSuper()
                        .create_user()
                        .create_lang()
                        .create_occupation()
                        .create_block_names()
                        .create_photo()
                        .create_header()
                        )
        logged_in = self.client.login(
            username = self.builder.username,
            password = self.builder.password,
            )
        self.assertTrue(logged_in)


    def test_get(self):
        url = reverse("cvs:header")
        response = self.client.get(url + "?lang=eng")
        actual_header = json.loads(response.content.decode())
        actual_photo = actual_header.pop("photo")

        expected_photo = {
            'photo': {
                'photo_url': '/media/photos/'
                }
            }
        self.assertIn(expected_photo["photo"]["photo_url"], actual_photo["photo_url"])
        self.assertEqual(actual_header, header_user_super._asdict())
