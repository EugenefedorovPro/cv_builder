from collections import namedtuple

ProjectTuple = namedtuple("ProjectTuple", ("project_name", "project_text", "web_url", "git_url"))

USER_SUPER = {
    "username": "user_super",
    "password": "user_super_password_1234",
    "is_superuser": True,
    }

USER_SIMPLE = {
    "username": "user_simple",
    "password": "user_simple_password_1234",
    "is_superuser": False,

    }

BLOCK_NAME_ENG: dict[str, str] = {
    "header_name": "Header",
    "hard_skills_name": "Hard Skills",
    "manifest_name": "Manifest",
    "projects_name": "Projects",
    "experience_name": "Experience",
    "soft_skills_name": "Soft Skills",
    "education_name": "Education",
    "hobby_name": "Hobby",
    "cases_name": "Cases",
    "why_me_name": "Why me?",
    }

PHOTO = {
    "description": "test_photo_super",
    "name": "test_image.jpg",
    "width": 150,
    "height": 200,
    "color": "Red",
    "mode": "RGB",
    "format": "JPEG",

    }

HEADER_USER_SUPER = {
    "first_name": "Eugene",
    "second_name": "Proskulikov",
    "phone": "+38-(096)-464-3910",
    "email": "eugene.proskulikov@gmail.com",
    "linkedin": "https://www.linkedin.com/in/eugene-proskulikov-168050a4/",
    "github": "https://github.com/EugenefedorovPro/",
    "country": "Ukraine",
    "city": "Kyiv",
    "district": "Left Bank",

    }

HEADER_USER_SIMPLE = {
    "first_name": "user_simple_first_name",
    "second_name": "user_simple_second_name",
    "phone": "+0987654321",
    "email": "simple_user@gmail.com",
    "linkedin": "https://www.linkedin.com/in/user_simple",
    "github": "usersimple.github.com",
    "country": "Simpleland",
    "city": "Simplecity",
    "district": "Simpledistrict",
    }

HARD_SKILLS_SUPER = {
    'Backend': 'Python, Django, Django Rest Api',
    'Frontend': 'React, html, css, bootstrap, JS, JQuery',
    'NN and DataScience': 'Keras + TensorFlow  (GRU models), numpy, pandas, unstructured texts and media field analysis with LooqMe, Semantrum, R',
    'Databases': 'sqlite, MySql, Postgres',
    'DevOps': 'docker, git, nginx, gunicorn, daphne, Linux, CI/CD, SSL, servers setup: VPS, RaspberryPI ',
    'Backend Utilities': 'Redis, Celery (worker, beat), WebSocket',
    'Network Engineering': 'VPN (OpenVpn, Wireguard), eoip, Graphana + Prometeus, firewalls, vlans, networks building',
    'IDE': 'vim, PyCharm, Jupyter, GoogleColab',

    }

MANIFEST_ENG = """Backend Software Engineer with a strong understanding of frontend development,\
 an analytical background, and hands-on experience in Neural Network development."""

## PROJECT

project_1 = ProjectTuple(
    project_name = "Creative Website for Poetry",
    project_text = (
        "A Django-based web application that generates random "
        "verses from an original poetry corpus on each visit, "
        "contrasting them with the author's curated works to explore"
        " the boundary between randomness and deliberate expression. "
        "Deployed with Docker, Nginx, and SSL."
    ),
    web_url = "https://eupoetry.kyiv.ua/",
    git_url = "https://github.com/EugenefedorovPro/eu_poetry_website",
    )

project_2 = ProjectTuple(
    project_name = "App to Find Rhymes to a Word",
    project_text = (
        "An open-source Python project and web application "
        "that implements a custom rhyme theory to generate rhymes for Russian words "
        "using NLP, machine learning (PyTorch-based neural networks for transcription "
        "and stress detection), and optimized algorithms "
        "(generator-based data processing, multiprocessing,"
        " and OOP design patterns). Built with Django and deployed using Docker and Nginx."
    ),
    web_url = "http://rhyme.kyiv.ua/",
    git_url = "https://github.com/EugenefedorovPro/rhyme_rus",
    )

project_3 = ProjectTuple(
    project_name = "NN to Put Stress onto a Word",
    project_text = (
        "An open-source Python package that predicts the position of stress in any Russian word — "
        "including neologisms — using a neural network trained on parsed Wiktionary data. "
        "Built with TensorFlow/Keras and GRU layers, "
        "and powered by custom preprocessing and IPA phonetic encoding."
    ),
    web_url = "",
    git_url = "https://github.com/EugenefedorovPro/put_stress_rus",
    )

project_4 = ProjectTuple(
    project_name = "NN to Transcribe Words",
    project_text = (
        "An open-source Python package that converts any Russian word — "
        "including neologisms — into its International Phonetic Alphabet (IPA) transcription "
        "using a GRU-based neural network with 99.96% categorical accuracy. "
        "Built with TensorFlow/Keras and trained on a custom-parsed Russian Wiktionary dataset."
    ),
    web_url = "",
    git_url = "https://github.com/EugenefedorovPro/word2ipa_rus",
    )

project_5 = ProjectTuple(
    project_name = "Poll-Making Forms Platform",
    project_text = (
        "A web-based platform for creating and managing polls, "
        "similar to Google Forms, using Django, JavaScript, and MySQL. "
        "Implemented anonymous respondent tracking, "
        "duplicate response prevention via browser fingerprinting, "
        "and a custom admin panel with role-based access for poll creators and administrators. "
        "Optimized analytics processing for large datasets (270,000 pings) using multiprocessing "
        "and efficient ORM queries, reducing computation time from 7 to 2.3 seconds."
    ),
    web_url = "https://poll.eger.in.ua/",
    git_url = "",
    )

project_6 = ProjectTuple(
    project_name = "Custom Monitoring System",
    project_text = (
        "A real-time monitoring system, featuring asynchronous ping tracking, "
        "sound alerts for missed pings, and dynamic charts using React (TypeScript) "
        "for visualization. Leveraged Django with Redis for scalable backend processing and "
        "MySql for persistent data storage. Optimized analytics queries to process 270,000 pings in 2.3 seconds, "
        "with role-based access control for users and admins."
    ),
    web_url = "",
    git_url = "",
    )

project_7 = ProjectTuple(
    project_name = "C Data Structures and Algorithms for Python",
    project_text = (
        "Developed a library of algorithms and data structures "
        "(red-black tree, hash table, sorting, linked list, queue) in C, "
        "integrated as Python packages using Cython and Python’s C API."
    ),
    web_url = "",
    git_url = "https://github.com/EugenefedorovPro/c_algorithms_for_python",
    )

PROJECTS_ENG: dict[int, ProjectTuple] = {
    1: project_1,
    2: project_2,
    3: project_3,
    4: project_4,
    5: project_5,
    6: project_6,
    7: project_7,
    }
