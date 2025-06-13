import json

import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse
from cvs.tests.data import SOFT_SKILLS_ENG
from cvs.types import (CvSoftSkillsType,
                       SoftSkillItemType,
                       )
from cvs.models.models import BlockNames


class SoftSkillTest(TestCase):
    def setUp(self):
        self.builder = TestBuilderSuper().create_user().create_lang().create_occupation().create_block_names().create_soft_skills()
        logged_in = self.client.login(username = self.builder.username, password = self.builder.password)
        self.assertTrue(logged_in)

    def test_soft_skills(self):
        url = reverse("cvs:soft_skills")
        response = self.client.get(url)
        actual_response = json.loads(response.content.decode())

        soft_skill_items: list[SoftSkillItemType] = []
        for item in SOFT_SKILLS_ENG:
            soft_skill_items.append(
                {
                    "id": item.id,
                    "soft_skill_text": item.soft_skill_text,

                    }
                )

        expected_response = [
            {
                'block_name': BlockNames.objects.all().first().soft_skills_name,

                },
            soft_skill_items,
            ]

        self.assertEqual(actual_response, expected_response)
