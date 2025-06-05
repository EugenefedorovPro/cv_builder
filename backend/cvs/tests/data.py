from collections import namedtuple
from datetime import datetime

ProjectTuple = namedtuple("ProjectTuple", (
    "project_name",
    "project_text",
    "web_url",
    "git_url",

    ))

ExperienceTuple = namedtuple("ExperienceTuple", (
    "id",
    "company",
    "start_date",
    "end_date",
    "position",
    "achievements",
    "order",

    ))

HardSkillTuple = namedtuple("HardSkillTuple", (
    "id",
    "category",
    "hard_skill_text",
    ))

SoftSkillTuple = namedtuple("SoftSkillTuple", (
    "id",
    "soft_skill_text",
    ))

EducationTuple = namedtuple("EducationTuple", (
    "id",
    "institution",
    "start_date",
    "end_date",
    "degree_title",
    ))

InterestTuple = namedtuple("InterestTuple", (
    "id",
    "interest_text",
    ))

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
    "interest_name": "Interest",
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

# hard skills

ANALYTICS_SKILLS = """Qualitative researchers: strategic sessions with fathers of business, in-depth interviews, focus-groups:
NLP, descriptive statistics in Python.
Authoring method of content-analysis.
Delivery of quantitative researches (google forms + R)
Supervision and briefing of research agencies.
"""

hard_skill_1 = HardSkillTuple(
    id = 1,
    category = "Backend",
    hard_skill_text = "Python, Django, Django Rest Api",

    )

hard_skill_2 = HardSkillTuple(
    id = 2,
    category = "Frontend",
    hard_skill_text = "React, html, css, bootstrap, JS, JQuery",

    )

hard_skill_3 = HardSkillTuple(
    id = 3,
    category = "NN and DataScience",
    hard_skill_text = "Keras + TensorFlow (GRU models), numpy, pandas, unstructured texts and media field analysis with LooqMe, Semantrum, R",

    )

hard_skill_4 = HardSkillTuple(
    id = 4,
    category = "Databases",
    hard_skill_text = "sqlite, MySql, Postgres",

    )

hard_skill_5 = HardSkillTuple(
    id = 5,
    category = "DevOps",
    hard_skill_text = "docker, git, nginx, gunicorn, daphne, Linux, CI/CD, SSL, servers setup: VPS, RaspberryPI",

    )

hard_skill_6 = HardSkillTuple(
    id = 6,
    category = "Backend Utilities",
    hard_skill_text = "Redis, Celery (worker, beat), WebSocket",
    )

hard_skill_7 = HardSkillTuple(
    id = 7,
    category = "Network Engineering",
    hard_skill_text = "VPN (OpenVpn, Wireguard), eoip, Graphana + Prometeus, firewalls, vlans, networks building",

    )

hard_skill_8 = HardSkillTuple(
    id = 8,
    category = "IDE",
    hard_skill_text = "vim, PyCharm, Jupyter, GoogleColab",

    )

hard_skill_9 = HardSkillTuple(
    id = 9,
    category = "Analytics",
    hard_skill_text = ANALYTICS_SKILLS,

    )

HARD_SKILLS_ENG = [
    hard_skill_1,
    hard_skill_2,
    hard_skill_3,
    hard_skill_4,
    hard_skill_5,
    hard_skill_6,
    hard_skill_7,
    hard_skill_8,
    hard_skill_9,

    ]

# manifest

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

# Experience
experience_1 = ExperienceTuple(
    id = 1,
    company = "Armed Forces of Ukraine",
    start_date = datetime(2022, 3, 22),
    end_date = None,
    position = "Sergeant in military communications",
    achievements = "Developed and maintained: software apps - monitoring system, platform for making polls",
    order = 0,
    )

ACHIEVEMENTS_2 = ("Launch of a new business in sport B1 Boxing Promotion: financial plan, "
                  "architecture of the brand, creative launch campaign, launch of SM")

experience_2 = ExperienceTuple(
    id = 2,
    company = "QuattrGroup",
    start_date = datetime(2020, 5, 1),
    end_date = datetime(2022, 3, 15),
    position = "Director Marketing, New Business Director, Member of Investment Board",
    achievements = ACHIEVEMENTS_2,
    order = 2,
    )

ACHIEVEMENTS_3 = """Research-driven communication strategies. 
Commercial sector - GEOS building company, Arzinger Law company, UMG (part of  SKM Group), 
Honda, Electrolux, OLX, Motorola Solutions, Київстар, Ocean Plaza, Amway, PepsiCo, Metro, etc.
NGOs: Dozorro, Crown Agents (state procurement). 
Public sector - Office of the Prosecutor General of Ukraine, Kiev city state council 
(marketing strategy to promote Kyiv as a tourist destination, communication strategy of Kyiv, campaign to promote General Plan of Kyiv), 
State Border Guard Service of Ukraine, Antimonopoly Committee of Ukraine 
(communication support of the State Aid Reform, SESAR project), 
state concept of crisis communications in partnership with Ministry of Information Policy and National Security and Defense Council of Ukraine, 
cybersecurity campaign for National Police 
"""

experience_3 = ExperienceTuple(
    id = 3,
    company = "RAM Group",
    start_date = datetime(2017, 9, 23),
    end_date = datetime(2020, 4, 12),
    position = "Strategic Director, Big Data Business Consultant, Analysts",
    achievements = ACHIEVEMENTS_3,
    order = 3,

    )

EXPERIENCE_ENG = [
    experience_1,
    experience_2,
    experience_3,

    ]

# Soft Skill
soft_skill_1 = SoftSkillTuple(
    id = 1,
    soft_skill_text = "Team-leader: I know how to motivate, develop clear and comprehensive brief, "
                      "provide feedback, persuade to fulfill the task in compliance with brief, "
                      "teach and support. Experienced in managing analytic, creative, content and SMM teams.",
    )

soft_skill_2 = SoftSkillTuple(
    id = 2,
    soft_skill_text = "I can work as an autonomous unit, "
                      "making up products on my own, "
                      "but when I work in a team, results turn out better",
    )

soft_skill_3 = SoftSkillTuple(
    id = 3,
    soft_skill_text = "I lean, therefore I am: Constant self-education in coding, analytics, and strategic thinking",

    )

SOFT_SKILLS_ENG = [
    soft_skill_1,
    soft_skill_2,
    soft_skill_3,

    ]

# education
education_1 = EducationTuple(
    id = 1,
    institution = "Kyiv State Linguistic University",
    start_date = datetime(1996, 11, 1),
    end_date = datetime(2001, 6, 1),
    degree_title = "Specialist in practical psychology, english philology with the right to teach the word literature",

    )

education_2 = EducationTuple(
    id = 2,
    institution = "Hryhoriy Skovoroda Institute of Philosophy of the Academy of Sciences of Ukraine",
    start_date = datetime(2005, 11, 1),
    end_date = datetime(2008, 7, 1),
    degree_title = "Successfully completed postgraduate studies in philosophy of ethics, aethetics and personality",

    )

EDUCATION_ENG = [
    education_1,
    education_2

    ]

# interests

interest_1 = InterestTuple(
    id = 1,
    interest_text = "Philosophy of Mind and AI"
    )

interest_2 = InterestTuple(
    id = 2,
    interest_text = "Avant-garde Art"
    )

INTERESTS_ENG = [
    interest_1,
    interest_2,

    ]
