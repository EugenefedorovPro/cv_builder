import json

import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse
from cvs.tests.data import NATURAL_LANGS_ENG

from cvs.types import NaturalLangItemType
from cvs.models.models import BlockNames


class NaturalLangTest(TestCase):
    def setUp(self):
        self.builder = TestBuilderSuper().create_user().create_lang().create_occupation().create_block_names().create_natural_lang()
        logged_in = self.client.login(username = self.builder.username, password = self.builder.password)
        self.assertTrue(logged_in)


    def test_natural_lang(self):
        url = reverse("cvs:natural_lang")
        response = self.client.get(url)
        actual = json.loads(response.content.decode())

        natural_lang_items: list[NaturalLangItemType] = []
        for item in NATURAL_LANGS_ENG:
            natural_lang_items.append(
                {
                    "id": item.id,
                    "natural_lang": item.natural_lang,
                    "level": item.level,

                    }
                )

        expected = [
            {
                'block_name': BlockNames.objects.all().first().natural_lang_name,

                },
            natural_lang_items,
            ]

        self.assertEqual(actual, expected)
