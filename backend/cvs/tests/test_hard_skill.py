import json

from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse
from cvs.tests.data import HARD_SKILLS_ENG
from cvs.types import HardSkilItemType

from cvs.models.models import BlockNames


class HardSkillTest(TestCase):
    def setUp(self):
        self.builder = TestBuilderSuper().create_user().create_lang().create_occupation().create_block_names().create_hard_skills()
        logged_in = self.client.login(username = self.builder.username, password = self.builder.password)
        self.assertTrue(logged_in)

    def test_hard_skills(self):
        url = reverse("cvs:hard_skills")
        response = self.client.get(url + "?lang=eng")
        actual_response = json.loads(response.content.decode())

        hard_skill_items: list[HardSkilItemType] = []
        for item in HARD_SKILLS_ENG:
            hard_skill_items.append(
                {
                    "id": item.id,
                    "category": item.category,
                    "hard_skill_text": item.hard_skill_text,

                    }
                )

        expected_response = [
            {
                'block_name': BlockNames.objects.all().first().hard_skills_name,

                },
            hard_skill_items,
            ]

        self.assertEqual(actual_response, expected_response)
