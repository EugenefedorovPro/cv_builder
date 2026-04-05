import json
from pprint import pprint

from django.test import TestCase
from django.urls import reverse

from .populate_test_db import TestBuilderSuper

expected = {
    "block_names": {"project_name": "Projects"},
    "projects": [
        {
            "id": 1,
            "project_name": "Creative Website for Poetry",
            "project_text": "A Django-based web application that generates random verses from an original poetry corpus on each visit, contrasting them with the author’s curated works. The project explores the boundary between randomness and intentional expression. Deployed with Docker, Nginx, and SSL.",
            "web_url": "https://eupoetry.kyiv.ua/",
            "git_url": "https://github.com/EugenefedorovPro/eu_poetry_website",
        },
        {
            "id": 2,
            "project_name": "App to Find Rhymes to a Word",
            "project_text": "An open-source Python project and web application that applies my personal new branded rhyme theory to generate rhymes for Russian words. It uses NLP and machine learning (Keras-based neural networks for transcription and stress detection), along with optimized algorithms such as generator-based data processing, multiprocessing, and OOP design patterns. Built with Django and deployed using Docker and Nginx.",
            "web_url": "http://rhyme.kyiv.ua/",
            "git_url": "https://github.com/EugenefedorovPro/rhyme_rus",
        },
        {
            "id": 3,
            "project_name": "NN to Put Stress onto a Word",
            "project_text": "An open-source Python package that predicts the stress position in any Russian word — including neologisms — using a neural network trained on parsed Wiktionary data. Developed with TensorFlow/Keras and GRU layers, enhanced by custom preprocessing and IPA-based phonetic encoding.",
            "web_url": "",
            "git_url": "https://github.com/EugenefedorovPro/put_stress_rus",
        },
        {
            "id": 4,
            "project_name": "NN to Transcribe Words",
            "project_text": "An open-source Python package that converts any Russian word - including neologisms - into its International Phonetic Alphabet (IPA) transcription using a GRU-based neural network with 99.96% categorical accuracy. Built with TensorFlow/Keras and trained on a custom-parsed Russian Wiktionary dataset.",
            "web_url": "",
            "git_url": "https://github.com/EugenefedorovPro/word2ipa_rus",
        },
        {
            "id": 5,
            "project_name": "Poll-Making Forms Platform",
            "project_text": "A web-based platform for creating and managing polls with no registration required, using browser fingerprinting to prevent duplicate responses. Features multiple question types, role-based access for poll creators and admins, and a custom admin panel with detailed analytics and CSV export. Optimized backend queries and Redis caching accelerate processing of large datasets, handling thousands of respondents efficiently. Built with Django, JavaScript, MySQL, deployed via Docker and Nginx with HTTPS security.",
            "web_url": "https://poll.eger.in.ua/",
            "git_url": "",
        },
        {
            "id": 6,
            "project_name": "Custom Monitoring System",
            "project_text": "A real-time monitoring system featuring asynchronous ping tracking, sound alerts for missed pings, and dynamic charts built with React (TypeScript). The backend uses Django with Redis for scalable processing and MySQL for data storage. Analytics are optimized to handle large datasets (270,000 pings) using multiprocessing and efficient ORM queries, reducing computation time from 7 to 2.3 seconds.",
            "web_url": "",
            "git_url": "",
        },
        {
            "id": 7,
            "project_name": "C Data Structures and Algorithms for Python",
            "project_text": "Developed a C library of algorithms and data structures (red-black tree, hash table, sorting, linked list, queue), integrated as Python packages using Cython and the Python C API.",
            "web_url": "",
            "git_url": "https://github.com/EugenefedorovPro/c_algorithms_for_python",
        },
    ],
}


class ProjectTest(TestCase):
    def setUp(self):
        self.builder = (
            TestBuilderSuper()
            .create_user()
            .create_lang()
            .create_occupation()
            .create_block_names()
            .create_projects()
        )
        logged_in = self.client.login(
            username=self.builder.username, password=self.builder.password
        )
        self.assertTrue(logged_in)

    def test_project(self):
        url = reverse("cvs:projects")
        response = self.client.get(url + "?lang=eng")
        actual = json.loads(response.content.decode())
        pprint(f"project_response = {actual}")
        self.assertEqual(actual, expected)
