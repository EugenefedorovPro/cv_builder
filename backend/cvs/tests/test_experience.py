import json
from pprint import pprint

import ipdb
from cvs.models.models import BlockNames
from cvs.tests.data import EXPERIENCE_ENG
from cvs.types import DATE_FORMATTER, CvExperienceType, ExperienceItemType
from django.test import TestCase
from django.urls import reverse

from .populate_test_db import TestBuilderSuper

expected = [
    {
        "block_names": {
            "achievements_title": "Achievements",
            "company_title": "Company",
            "exp_period_title": "Period",
            "experience_name": "Experience",
            "position_title": "Position",
        },
        "experience": [
            {
                "achievements": "Developed and maintained software "
                "applications including a monitoring system "
                "and a poll-making platform; designed and "
                "implemented a complex system for remote and "
                "secure server access via VPN.",
                "company": "Armed Forces of Ukraine",
                "end_date": None,
                "id": 1,
                "position": "Sergeant in Military Communications",
                "start_date": "2022-03-22",
            },
            {
                "achievements": "Led the conceptual development of the "
                "company’s and owner’s websites. Initiated "
                "and launched a new business in sports — B1 "
                "Boxing Promotion — including financial "
                "planning, brand architecture, a creative "
                "launch campaign, and social media "
                "activation.",
                "company": "QuattrGroup",
                "end_date": "2022-03-15",
                "id": 2,
                "position": "Director of Marketing, New Business Director, "
                "Member of the Investment Board",
                "start_date": "2020-05-01",
            },
            {
                "achievements": "Developed research-driven communication "
                "strategies for clients across public, "
                "commercial, and state sectors, including "
                "Honda, Electrolux, OLX, Київстар, and "
                "PepsiCo. Projects included: the Dozorro "
                "platform, a national cybersecurity campaign "
                "for the National Police, communication "
                "support for the State Aid Reform, the SESAR "
                "project for the Antimonopoly Committee of "
                "Ukraine, and initiatives with the Kyiv City "
                "State Administration. Co-authored the "
                "national crisis communications concept in "
                "partnership with the Ministry of "
                "Information Policy and the National "
                "Security and Defense Council of Ukraine.",
                "company": "RAM Group",
                "end_date": "2020-04-12",
                "id": 3,
                "position": "Strategic Director, Big Data Business "
                "Consultant, Analyst",
                "start_date": "2017-09-23",
            },
        ],
    }
]


class ExperienceTest(TestCase):
    def setUp(self):
        self.builder = (
            TestBuilderSuper()
            .create_user()
            .create_lang()
            .create_occupation()
            .create_block_names()
            .create_experience()
        )
        logged_in = self.client.login(
            username=self.builder.username, password=self.builder.password
        )
        self.assertTrue(logged_in)

    def test_experience(self):
        url = reverse("cvs:experience")
        response = self.client.get(url + "?lang=eng")
        actual = json.loads(response.content.decode())
        pprint(f"experience_response = {actual}")
        self.assertEqual(actual, expected)
