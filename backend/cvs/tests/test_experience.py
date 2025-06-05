import json

import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse
from cvs.tests.data import EXPERIENCE_ENG
from cvs.types import (ExperienceItemType,
                       CvExperienceType, DATE_FORMATTER,
                       )


class ExperienceTest(TestCase):
    def setUp(self):
        self.builder = TestBuilderSuper().create_user().create_lang().create_block_names().create_experience()
        logged_in = self.client.login(username = self.builder.username, password = self.builder.password)
        self.assertTrue(logged_in)


    def test_experience(self):
        url = reverse("cvs:experience")
        response = self.client.get(url)
        actual = json.loads(response.content.decode())

        expected_projects: list[ExperienceItemType] = []
        for item in EXPERIENCE_ENG:
            expected_projects.append({
                "id": item.id,
                "company": item.company,
                "position": item.position,
                "start_date": item.start_date.strftime(DATE_FORMATTER),
                "end_date": item.end_date.strftime(DATE_FORMATTER) if item.end_date else None,
                "achievements": item.achievements,

                })
        expected: CvExperienceType = [
            {
                'block_name': 'Experience'
                },
            expected_projects,
            ]

        self.assertEqual(actual, expected)
