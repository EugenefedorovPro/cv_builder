import ipdb
from django.test import TestCase
from cvs.models.models import Header
from .populate_test_db import PrepareTestData
from django.shortcuts import reverse


class HeaderTest(PrepareTestData):
    def test_users_access(self):
        """User must have access to their own header, not to others."""
        logged_in = self.client.login(username = self.user_simple_username, password = self.user_simple_password)
        self.assertTrue(logged_in)
        url = reverse("admin:cvs_header_changelist")
        response = self.client.get(url, follow = True)
        response_content = response.content.decode()
        ipdb.set_trace()


