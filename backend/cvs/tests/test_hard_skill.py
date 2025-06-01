import json

import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse


class HardSkillTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.builder = TestBuilderSuper().create_user().create_lang().create_block_names().create_hard_skills()

    def setUp(self):
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
                'hard_skill_text': 'Python, Django, Django Rest Api',
                'id': 1
                },
                {
                    'category': 'Frontend',
                    'hard_skill_text': 'React, html, css, bootstrap, JS, JQuery',
                    'id': 2
                    },
                {
                    'category': 'NN and DataScience',
                    'hard_skill_text': 'Keras + TensorFlow  (GRU models), numpy, pandas, '
                                       'unstructured texts and media field analysis with '
                                       'LooqMe, Semantrum, R',
                    'id': 3
                    },
                {
                    'category': 'Databases',
                    'hard_skill_text': 'sqlite, MySql, Postgres',
                    'id': 4
                    },
                {
                    'category': 'DevOps',
                    'hard_skill_text': 'docker, git, nginx, gunicorn, daphne, Linux, CI/CD, '
                                       'SSL, servers setup: VPS, RaspberryPI ',
                    'id': 5
                    },
                {
                    'category': 'Backend Utilities',
                    'hard_skill_text': 'Redis, Celery (worker, beat), WebSocket',
                    'id': 6
                    },
                {
                    'category': 'Network Engineering',
                    'hard_skill_text': 'VPN (OpenVpn, Wireguard), eoip, Graphana + Prometeus, '
                                       'firewalls, vlans, networks building',
                    'id': 7
                    },
                {
                    'category': 'IDE',
                    'hard_skill_text': 'vim, PyCharm',
                    'id': 8
                    }]]

        self.assertEqual(actual_response, expected_response)
