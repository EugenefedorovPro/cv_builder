import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from django.contrib.auth import get_user_model
from cvs.models.models import (BlockNames,
                               Header,
                               )
from django.shortcuts import reverse

User = get_user_model()


# @skip("")
class GenerateDocxTest(TestCase):
    def setUp(self):
        self.builder = (TestBuilderSuper()
                        .create_user()
                        .create_lang()
                        .create_occupation()
                        .create_block_names()
                        .create_photo()
                        .create_header()
                        .create_manifest()
                        .create_hard_skills()
                        .create_projects()
                        .create_experience()
                        .create_soft_skills()
                        .create_education()
                        .create_interest()
                        .create_natural_lang()
                        )
        logged_in = self.client.login(
            username = self.builder.username,
            password = self.builder.password,
            )
        self.assertTrue(logged_in)

    def write_docx(self):
        url = reverse("cvs:generate_docx")
        response = self.client.get(url + "?lang=eng")

        with open("test_cv.docx", "wb") as f:
            f.write(response.content)
        return response


    def test_get(self):
        response = self.write_docx()
        expected = '<HttpResponse status_code=200, "application/vnd.openxmlformats-officedocument.wordprocessingml.document">'
        self.assertEqual(expected, str(response))

    def test_get_void_in_header(self):
        """no city and district fields in BlockNames and Header"""
        lang = "eng"

        block_names = BlockNames.objects.filter(lang__lang = lang).first()
        block_names.city_title = ""
        block_names.district_title = None
        block_names.country_title = ""
        block_names.save()

        header = Header.objects.filter(lang__lang = lang).first()
        header.city = None
        header.district = None
        header.country = ""
        header.save()

        self.write_docx()
