import json

import ipdb
from django.shortcuts import reverse
from django.test import TestCase

from cvs.models.models import BlockNames
from cvs.tests.data import NATURAL_LANGS_ENG
from cvs.types import NaturalLangItemType

from .populate_test_db import TestBuilderSuper

expected = {
    "block_names": {"natural_lang_name": "Natural Languages"},
    "natural_langs": [
        {"id": 1, "level": "ready to deliver interview", "natural_lang": "English"},
        {"id": 2, "level": "fluent", "natural_lang": "Ukrainian"},
        {"id": 3, "level": "fluent", "natural_lang": "Russian"},
        {"id": 4, "level": "basic", "natural_lang": "German"},
    ],
}


class NaturalLangTest(TestCase):
    def setUp(self):
        self.builder = (
            TestBuilderSuper()
            .create_user()
            .create_lang()
            .create_occupation()
            .create_block_names()
            .create_natural_lang()
        )
        logged_in = self.client.login(
            username=self.builder.username, password=self.builder.password
        )
        self.assertTrue(logged_in)

    def test_natural_lang(self):
        url = reverse("cvs:natural_lang")
        response = self.client.get(url + "?lang=eng")
        actual = json.loads(response.content.decode())
        self.assertEqual(actual, expected)
