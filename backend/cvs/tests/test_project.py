import json

import ipdb
from django.test import TestCase
from .populate_test_db import TestBuilderSuper
from django.shortcuts import reverse
from cvs.tests.data import (PROJECTS_ENG,
                            ProjectTuple,
                            )
from cvs.types import (ProjectItemType,
                       CvProjectType,
                       )


class ProjectTest(TestCase):
    def setUp(self):
        self.builder = TestBuilderSuper().create_user().create_lang().create_block_names().create_projects()
        logged_in = self.client.login(username = self.builder.username, password = self.builder.password)
        self.assertTrue(logged_in)


    def test_project(self):
        url = reverse("cvs:projects")
        response = self.client.get(url)
        actual = json.loads(response.content.decode())

        expected_projects: list[ProjectItemType] = []
        for idx in range(len(PROJECTS_ENG)):
            expected_projects.append({
                "id": idx + 1,
                "project_name": PROJECTS_ENG[idx + 1].project_name,
                "project_text": PROJECTS_ENG[idx + 1].project_text,
                "web_url": PROJECTS_ENG[idx + 1].web_url,
                "git_url": PROJECTS_ENG[idx + 1].git_url,
                })
        expected: CvProjectType = [
            {
                'block_name': 'Projects'
                },
            expected_projects,
            ]

        self.assertEqual(actual, expected)
