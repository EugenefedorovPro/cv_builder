import json

import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse
from cvs.tests.data import EDUCATION_ENG
from cvs.types import (EducationItemType,
                       DATE_FORMATTER,
                       )

from cvs.models.models import BlockNames


class EducationTest(TestCase):
    def setUp(self):
        self.builder = TestBuilderSuper().create_user().create_lang().create_occupation().create_block_names().create_education()
        logged_in = self.client.login(username = self.builder.username, password = self.builder.password)
        self.assertTrue(logged_in)


    def test_education(self):
        url = reverse("cvs:education")
        response = self.client.get(url + "?lang=eng")
        actual = json.loads(response.content.decode())

        education_items: list[EducationItemType] = []
        for item in EDUCATION_ENG:
            education_items.append(
                {
                    "id": item.id,
                    "institution": item.institution,
                    "start_date": item.start_date.strftime(DATE_FORMATTER),
                    "end_date": item.end_date.strftime(DATE_FORMATTER),
                    "degree_title": item.degree_title,
                    }
                )

        expected = [
            {
                'block_name': BlockNames.objects.all().first().education_name,

                },
            education_items,
            ]

        self.assertEqual(actual, expected)
