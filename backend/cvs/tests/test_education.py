import json

from django.shortcuts import reverse
from django.test import TestCase

from .populate_test_db import TestBuilderSuper

expected = {
    "block_names": {"education_name": "Education"},
    "education": [
        {
            "degree_title": "Specialist in Practical Psychology and "
            "English Philology, with teaching "
            "qualification in World Literature",
            "end_date": "2001-06-01",
            "id": 1,
            "institution": "Kyiv State Linguistic University",
            "start_date": "1996-11-01",
        },
        {
            "degree_title": "Completed postgraduate studies in Philosophy "
            "with a focus on Ethics, Aesthetics, and "
            "Personality",
            "end_date": "2008-07-01",
            "id": 2,
            "institution": "Hryhoriy Skovoroda Institute of Philosophy, "
            "National Academy of Sciences of Ukraine",
            "start_date": "2005-11-01",
        },
    ],
}


class EducationTest(TestCase):
    def setUp(self):
        self.builder = (
            TestBuilderSuper()
            .create_user()
            .create_lang()
            .create_occupation()
            .create_block_names()
            .create_education()
        )
        logged_in = self.client.login(
            username=self.builder.username, password=self.builder.password
        )
        self.assertTrue(logged_in)

    def test_education(self):
        url = reverse("cvs:education")
        response = self.client.get(url + "?lang=eng")
        actual = json.loads(response.content.decode())
        self.assertEqual(actual, expected)
