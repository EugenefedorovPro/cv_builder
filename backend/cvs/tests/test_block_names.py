import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from cvs.tests.data import block_name_eng
from django.contrib.auth import get_user_model
from cvs.models.models import BlockNames

User = get_user_model()


class BlockNamesTest(TestCase):
    def setUp(self):
        self.builder = (TestBuilderSuper()
                        .create_user()
                        .create_lang()
                        .create_occupation()
                        .create_block_names()
                        )
        logged_in = self.client.login(
            username = self.builder.username,
            password = self.builder.password,
            )
        self.assertTrue(logged_in)


    def test_get(self):
        actual = BlockNames.objects.all().first()
        expected = block_name_eng

        self.assertEqual(expected.cases_name, actual.cases_name)
        self.assertEqual(expected.education_name, actual.education_name)
        self.assertEqual(expected.experience_name, actual.experience_name)
        self.assertEqual(expected.feedback_name, actual.feedback_name)
        self.assertEqual(expected.hard_skills_name, actual.hard_skills_name)
        self.assertEqual(expected.header_name, actual.header_name)
        self.assertEqual(expected.interest_name, actual.interest_name)
        self.assertEqual(expected.manifest_name, actual.manifest_name)
        self.assertEqual(expected.natural_lang_name, actual.natural_lang_name)
        self.assertEqual(expected.photo_name, actual.photo_name)
        self.assertEqual(expected.projects_name, actual.projects_name)
        self.assertEqual(expected.soft_skills_name, actual.soft_skills_name)
        self.assertEqual(expected.why_me_name, actual.why_me_name)
