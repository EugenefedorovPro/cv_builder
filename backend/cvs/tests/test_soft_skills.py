import json

import ipdb
from django.shortcuts import reverse
from django.test import TestCase

from cvs.models.models import BlockNames
from cvs.tests.data import SOFT_SKILLS_ENG
from cvs.types import CvSoftSkillsType, SoftSkillItemType

from .populate_test_db import TestBuilderSuper

expected = {
    "block_names": {"soft_skills_name": "Soft Skills"},
    "soft_skills": [
        {
            "id": 1,
            "soft_skill_text": "Skilled at motivating others, developing "
            "clear and comprehensive briefs, "
            "providing constructive feedback, and "
            "ensuring task completion aligned with "
            "objectives. Experienced in managing "
            "analytics, creative, content, and SMM "
            "teams.",
        },
        {
            "id": 2,
            "soft_skill_text": "Capable of working independently to "
            "develop complete products, while "
            "achieving even better results in "
            "collaborative team environments.",
        },
        {
            "id": 3,
            "soft_skill_text": "I learn, therefore I am: committed to "
            "continuous self-education in coding, "
            "analytics, and strategic thinking.",
        },
    ],
}


class SoftSkillTest(TestCase):
    def setUp(self):
        self.builder = (
            TestBuilderSuper()
            .create_user()
            .create_lang()
            .create_occupation()
            .create_block_names()
            .create_soft_skills()
        )
        logged_in = self.client.login(
            username=self.builder.username, password=self.builder.password
        )
        self.assertTrue(logged_in)

    def test_soft_skills(self):
        url = reverse("cvs:soft_skills")
        response = self.client.get(url + "?lang=eng")
        actual = json.loads(response.content.decode())
        self.assertEqual(actual, expected)
