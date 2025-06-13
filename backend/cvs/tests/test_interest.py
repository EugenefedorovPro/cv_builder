import json

import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse
from cvs.tests.data import (INTERESTS_ENG,
                            InterestTuple,
                            )
from cvs.types import (InterestItemType,
                       CvInterestType,
                       DATE_FORMATTER,
                       )
from cvs.models.models import BlockNames


class InterestTest(TestCase):
    def setUp(self):
        self.builder = TestBuilderSuper().create_user().create_lang().create_occupation().create_block_names().create_interest()
        logged_in = self.client.login(username = self.builder.username, password = self.builder.password)
        self.assertTrue(logged_in)


    def test_interest(self):
        url = reverse("cvs:interest")
        response = self.client.get(url)
        actual = json.loads(response.content.decode())

        interest_items: list[InterestItemType] = []
        for item in INTERESTS_ENG:
            interest_items.append(
                {
                    "id": item.id,
                    "interest_text": item.interest_text,
                    }
                )

        expected = [
            {
                'block_name': BlockNames.objects.all().first().interest_name,

                },
            interest_items,
            ]

        self.assertEqual(actual, expected)
