import json
from pprint import pprint
import ipdb
from cvs.models.models import BlockNames
from cvs.tests.data import HARD_SKILLS_ENG
from cvs.types import HardSkilItemType
from django.test import TestCase
from django.urls import reverse

from .populate_test_db import TestBuilderSuper

expected_response = {
    "block_names": {"hard_skills_name": "Hard Skills"},
    "hard_skills": [
        {
            "category": "Backend",
            "hard_skill_text": "Python, Django, Django REST API",
            "id": 1,
        },
        {
            "category": "Frontend",
            "hard_skill_text": "React, HTML, CSS, Bootstrap, JavaScript, " "jQuery",
            "id": 2,
        },
        {
            "category": "NN and DataScience",
            "hard_skill_text": "Keras + TensorFlow (GRU models), NumPy, "
            "pandas. Media and unstructured text "
            "analysis using LooqMe, Semantrum, and R",
            "id": 3,
        },
        {
            "category": "Databases",
            "hard_skill_text": "SQLite, MySQL, PostgreSQL",
            "id": 4,
        },
        {
            "category": "DevOps",
            "hard_skill_text": "Docker, Git, Nginx, Gunicorn, Daphne, "
            "Linux, CI/CD pipelines, SSL. Server "
            "setup on VPS and Raspberry Pi.",
            "id": 5,
        },
        {
            "category": "Backend Utilities",
            "hard_skill_text": "Redis, Celery (worker and beat), " "WebSocket",
            "id": 6,
        },
        {
            "category": "Network Engineering",
            "hard_skill_text": "VPN (OpenVPN, WireGuard), EoIP, Grafana "
            "+ Prometheus, firewalls, VLANs, network "
            "architecture and deployment",
            "id": 7,
        },
        {
            "category": "IDE",
            "hard_skill_text": "Vim, PyCharm, Jupyter Notebook, Google " "Colab",
            "id": 8,
        },
        {
            "category": "Analytics",
            "hard_skill_text": "Experienced in qualitative research: "
            "strategic sessions with business "
            "leaders, in-depth interviews, and focus "
            "groups. Skilled Python-based descriptive "
            "statistics. Developed a custom method of "
            "content analysis. Delivered quantitative "
            "research using Google Forms and R. "
            "Managed and briefed external research "
            "agencies.",
            "id": 9,
        },
        {
            "category": "Authoring training programs",
            "hard_skill_text": "Designed training programs on "
            "copywriting, strategic planning, crisis "
            "communication, and creative management. "
            "Conducted at PR School (Kyiv Polytechnic "
            "Institute), Energoatom, Galnaftogaz, "
            "Amway, State Border Guard Service, and "
            "Ministry of Internal Affairs agencies.",
            "id": 10,
        },
    ],
}


class HardSkillTest(TestCase):
    def setUp(self):
        self.builder = (
            TestBuilderSuper()
            .create_user()
            .create_lang()
            .create_occupation()
            .create_block_names()
            .create_hard_skills()
        )
        logged_in = self.client.login(
            username=self.builder.username, password=self.builder.password
        )
        self.assertTrue(logged_in)

    def test_hard_skills(self):
        url = reverse("cvs:hard_skills")
        response = self.client.get(url + "?lang=eng")
        actual_response = json.loads(response.content.decode())
        pprint(f"hard_skills_response = {actual_response}")
        self.assertEqual(actual_response, expected_response)

