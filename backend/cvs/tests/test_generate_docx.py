import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from cvs.tests.data import block_name_eng
from django.contrib.auth import get_user_model
from cvs.models.models import BlockNames
from django.shortcuts import reverse

User = get_user_model()


class GenerateDocxTest(TestCase):
    def setUp(self):
        self.builder = (TestBuilderSuper()
                        .create_user()
                        .create_lang()
                        .create_occupation()
                        .create_block_names()
                        .create_manifest()
                        )
        logged_in = self.client.login(
            username = self.builder.username,
            password = self.builder.password,
            )
        self.assertTrue(logged_in)


    def test_get(self):
        url = reverse("cvs:generate_docx")
        response = self.client.get(url)
        ipdb.set_trace()
        expected = '<HttpResponse status_code=200, "application/vnd.openxmlformats-officedocument.wordprocessingml.document">'
        self.assertEqual(expected, str(response))
