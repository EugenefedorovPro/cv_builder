import json
from pprint import pprint
from unittest import mock, skip

import ipdb
from django.test import TestCase
from django.urls import reverse

from cvs.models.models import CustomUser
from cvs.types import CustomUserType

from .populate_test_db import TestBuilderSuper


class TestOccupation(TestCase):

    def setUp(self):
        self.builder = TestBuilderSuper().create_user()
        logged_in = self.client.login(
            username=self.builder.username,
            password=self.builder.password,
        )
        self.assertTrue(logged_in)

    # @skip("")
    @mock.patch("cvs.views.component_views.UuidUrl.objects.get_or_create")
    def test_post(self, mock_get_or_create_uuid_url):
        uuid_url_mock = "mocked_uuid_url_1234"
        mock_uuid_obj = mock.MagicMock()
        mock_uuid_obj.uuid_url = uuid_url_mock
        mock_get_or_create_uuid_url.return_value = (mock_uuid_obj, True)

        url = reverse("cvs:occupation_choice")
        data = {
            "occupation": "full-stack",
        }
        response = self.client.post(url, data=data)
        expected_occupation_data = {"id": 1, "occupation": "full-stack"}

        self.assertEqual(expected_occupation_data, response.data["occupation_data"])
        self.assertEqual(uuid_url_mock, response.data["uuid_url"])
