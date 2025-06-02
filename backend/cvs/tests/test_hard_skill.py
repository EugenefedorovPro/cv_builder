import json

import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse
from cvs.tests.data import HARD_SKILLS_SUPER


class HardSkillTest(TestCase):
    def setUp(self):
        self.builder = TestBuilderSuper().create_user().create_lang().create_block_names().create_hard_skills()
        logged_in = self.client.login(username = self.builder.username, password = self.builder.password)
        self.assertTrue(logged_in)

    def test_hard_skills(self):
        self.maxDiff = True
        url = reverse("cvs:hard_skills")
        response = self.client.get(url)
        actual_response = json.loads(response.content.decode())
        expected_response = [{
            'block_name': 'Hard Skills'
            },
            [{
                'category': 'Backend',
                'hard_skill_text': HARD_SKILLS_SUPER['Backend'],
                'id': 1
                },
                {
                    'category': 'Frontend',
                    'hard_skill_text': HARD_SKILLS_SUPER['Frontend'],
                    'id': 2
                    },
                {
                    'category': 'NN and DataScience',
                    'hard_skill_text': HARD_SKILLS_SUPER['NN and DataScience'],
                    'id': 3
                    },
                {
                    'category': 'Databases',
                    'hard_skill_text': HARD_SKILLS_SUPER['Databases'],
                    'id': 4
                    },
                {
                    'category': 'DevOps',
                    'hard_skill_text': HARD_SKILLS_SUPER['DevOps'],
                    'id': 5
                    },
                {
                    'category': 'Backend Utilities',
                    'hard_skill_text': HARD_SKILLS_SUPER['Backend Utilities'],
                    'id': 6
                    },
                {
                    'category': 'Network Engineering',
                    'hard_skill_text': HARD_SKILLS_SUPER['Network Engineering'],
                    'id': 7
                    },
                {
                    'category': 'IDE',
                    'hard_skill_text': HARD_SKILLS_SUPER['IDE'],
                    'id': 8
                    }]]

        self.assertEqual(actual_response, expected_response)
