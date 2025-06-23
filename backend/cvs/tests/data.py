from collections import namedtuple
from datetime import datetime
from cvs.types import (ProjectTuple,
                       ExperienceTuple,
                       HardSkillTuple,
                       SoftSkillTuple,
                       EducationTuple,
                       InterestTuple,
                       NaturalLangTuple,
                       OccupationChoiceTuple,
                       HeaderTuple,
                       PhotoTuple,
                       BlockNameTuple,
                       ManifestTuple,
                       )


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

OCCUPATION_ENG = OccupationChoiceTuple(
    id = 1,
    occupation = "Backend",

    )

block_name_eng = BlockNameTuple(
    id = 1,
    photo_name = "Photo",
    header_name = "Header",
    hard_skills_name = "Hard Skills",
    manifest_name = "Manifest",
    projects_name = "Projects",
    experience_name = "Experience",
    soft_skills_name = "Soft Skills",
    education_name = "Education",
    natural_lang_name = "Natural Languages",
    interest_name = "Interests",
    cases_name = "Cases",
    why_me_name = "Why me?",
    feedback_name = "Feedback",
    country_title = "Country: ",
    city_title = "City: ",
    district_title = "District: ",
    company_title = "Company",
    exp_period_title = "Period",
    position_title = "Position",
    achievements_title = "Achievements",
    institution_title = "Institution",
    ed_period_title = "Period",
    degree_title = "Degree",
    level_title = "level: ",
    task_title = "Task",
    solution_title = "Solution",
    optimization_title = "Optimization",
    result_title = "Result",
    tech_stack_title = "Tech Stack",
    contacts_title = "Contacts",
    current = "current",
    )

BLOCK_NAMES: list[BlockNameTuple] = [
    block_name_eng,

    ]

PHOTO_ENG = PhotoTuple(
    id = 1,
    description = "test_photo_super",
    name = "test_image.jpg",
    width = 150,
    height = 200,
    color = "Red",
    mode = "RGB",
    format = "JPEG",
    )

header_user_super = HeaderTuple(
    id = 1,
    first_name = "Eugene",
    second_name = "Proskulikov",
    phone = "+38-(096)-464-3910",
    email = "eugene.proskulikov@gmail.com",
    linkedin = "https://www.linkedin.com/in/eugene-proskulikov-168050a4/",
    github = "https://github.com/EugenefedorovPro/",
    country = "Ukraine",
    city = "Kyiv",
    district = "Left Bank",

    )

header_user_simple = HeaderTuple(
    id = 2,
    first_name = "user_simple_first_name",
    second_name = "user_simple_second_name",
    phone = "+0987654321",
    email = "simple_user@gmail.com",
    linkedin = "https://www.linkedin.com/in/user_simple",
    github = "usersimple.github.com",
    country = "Simpleland",
    city = "Simplecity",
    district = "Simpledistrict",

    )

HEADERS_ENG: list[HeaderTuple] = [
    header_user_super,

    ]

# hard skills

ANALYTICS_SKILLS = (
    "Experienced in qualitative research: strategic sessions with business leaders, in-depth interviews, and focus groups. "
    "Skilled Python-based descriptive statistics. Developed a custom method of content analysis. "
    "Delivered quantitative research using Google Forms and R. Managed and briefed external research agencies."
)

hard_skill_1 = HardSkillTuple(
    id = 1,
    category = "Backend",
    hard_skill_text = "Python, Django, Django REST API",

    )

hard_skill_2 = HardSkillTuple(
    id = 2,
    category = "Frontend",
    hard_skill_text = "React, HTML, CSS, Bootstrap, JavaScript, jQuery",

    )

hard_skill_3 = HardSkillTuple(
    id = 3,
    category = "NN and DataScience",
    hard_skill_text = (
        "Keras + TensorFlow (GRU models), NumPy, pandas. "
        "Media and unstructured text analysis using LooqMe, Semantrum, and R"
    ))

hard_skill_4 = HardSkillTuple(
    id = 4,
    category = "Databases",
    hard_skill_text = "SQLite, MySQL, PostgreSQL",

    )

hard_skill_5 = HardSkillTuple(
    id = 5,
    category = "DevOps",
    hard_skill_text = (
        "Docker, Git, Nginx, Gunicorn, Daphne, Linux, "
        "CI/CD pipelines, SSL. Server setup on VPS and Raspberry Pi.")

    )

hard_skill_6 = HardSkillTuple(
    id = 6,
    category = "Backend Utilities",
    hard_skill_text = "Redis, Celery (worker and beat), WebSocket",
    )

hard_skill_7 = HardSkillTuple(
    id = 7,
    category = "Network Engineering",
    hard_skill_text = (
        "VPN (OpenVPN, WireGuard), EoIP, Grafana + Prometheus, firewalls, "
        "VLANs, network architecture and deployment")
    )

hard_skill_8 = HardSkillTuple(
    id = 8,
    category = "IDE",
    hard_skill_text = "Vim, PyCharm, Jupyter Notebook, Google Colab",

    )

hard_skill_9 = HardSkillTuple(
    id = 9,
    category = "Analytics",
    hard_skill_text = ANALYTICS_SKILLS,

    )

TRAININGS = (
    "Designed training programs on copywriting, strategic planning, crisis communication, and creative management. "
    "Conducted at PR School (Kyiv Polytechnic Institute), Energoatom, Galnaftogaz, "
    "Amway, State Border Guard Service, and Ministry of Internal Affairs agencies."
)

hard_skill_10 = HardSkillTuple(
    id = 10,
    category = "Authoring training programs",
    hard_skill_text = TRAININGS,

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
    hard_skill_10,

    ]

# manifest

MANIFEST_ENG = ManifestTuple(
    id = 1,
    manifest_text =
    "Backend Software Engineer with a strong grasp of frontend development, "
    "a solid analytical background, and practical experience in neural network development"

    )

## PROJECT

project_1 = ProjectTuple(
    project_name = "Creative Website for Poetry",
    project_text = (
        "A Django-based web application that generates random verses "
        "from an original poetry corpus on each visit, contrasting them "
        "with the author’s curated works. The project explores the boundary "
        "between randomness and intentional expression. Deployed with Docker, "
        "Nginx, and SSL."
    ),
    web_url = "https://eupoetry.kyiv.ua/",
    git_url = "https://github.com/EugenefedorovPro/eu_poetry_website",
    )

project_2 = ProjectTuple(
    project_name = "App to Find Rhymes to a Word",
    project_text = (
        "An open-source Python project and web application that applies my personal new branded rhyme theory "
        "to generate rhymes for Russian words. It uses NLP and machine learning (Keras-based "
        "neural networks for transcription and stress detection), along with optimized algorithms "
        "such as generator-based data processing, multiprocessing, and OOP design patterns. "
        "Built with Django and deployed using Docker and Nginx."
    ),
    web_url = "http://rhyme.kyiv.ua/",
    git_url = "https://github.com/EugenefedorovPro/rhyme_rus",
    )

project_3 = ProjectTuple(
    project_name = "NN to Put Stress onto a Word",
    project_text = (
        "An open-source Python package that predicts the stress position in any Russian word — "
        "including neologisms — using a neural network trained on parsed Wiktionary data. "
        "Developed with TensorFlow/Keras and GRU layers, enhanced by custom preprocessing "
        "and IPA-based phonetic encoding."
    ),
    web_url = "",
    git_url = "https://github.com/EugenefedorovPro/put_stress_rus",
    )

project_4 = ProjectTuple(
    project_name = "NN to Transcribe Words",
    project_text = (
        "An open-source Python package that converts any Russian word - "
        "including neologisms - into its International Phonetic Alphabet (IPA) transcription "
        "using a GRU-based neural network with 99.96% categorical accuracy. "
        "Built with TensorFlow/Keras and trained on a custom-parsed Russian Wiktionary dataset."
    ),
    web_url = "",
    git_url = "https://github.com/EugenefedorovPro/word2ipa_rus",
    )

project_5 = ProjectTuple(
    project_name = "Poll-Making Forms Platform",
    project_text = (
        "A web-based platform for creating and managing polls with no registration required, "
        "using browser fingerprinting to prevent duplicate responses. "
        "Features multiple question types, role-based access for poll creators and admins, "
        "and a custom admin panel with detailed analytics and CSV export. "
        "Optimized backend queries and Redis caching accelerate processing of large datasets, "
        "handling thousands of respondents efficiently. Built with Django, JavaScript, MySQL, "
        "deployed via Docker and Nginx with HTTPS security."
    ),
    web_url = "https://poll.eger.in.ua/",
    git_url = "",
    )

project_6 = ProjectTuple(
    project_name = "Custom Monitoring System",
    project_text = (
        "A real-time monitoring system featuring asynchronous ping tracking, "
        "sound alerts for missed pings, and dynamic charts built with React (TypeScript). "
        "The backend uses Django with Redis for scalable processing and MySQL for data storage. "
        "Analytics are optimized to handle large datasets (270,000 pings) using multiprocessing "
        "and efficient ORM queries, reducing computation time from 7 to 2.3 seconds."
    ),
    web_url = "",
    git_url = "",
    )

project_7 = ProjectTuple(
    project_name = "C Data Structures and Algorithms for Python",
    project_text = (
        "Developed a C library of algorithms and data structures "
        "(red-black tree, hash table, sorting, linked list, queue), "
        "integrated as Python packages using Cython and the Python C API."
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

ACHIEVEMENTS_1 = (
    "Developed and maintained software applications including a monitoring system and a poll-making platform; "
    "designed and implemented a complex system for remote and secure server access via VPN."
)

experience_1 = ExperienceTuple(
    id = 1,
    company = "Armed Forces of Ukraine",
    start_date = datetime(2022, 3, 22),
    end_date = None,
    position = "Sergeant in Military Communications",
    achievements = ACHIEVEMENTS_1,
    order = 0,
    )

ACHIEVEMENTS_2 = (
    "Led the conceptual development of the company’s and owner’s websites. "
    "Initiated and launched a new business in sports — B1 Boxing Promotion — including financial planning, "
    "brand architecture, a creative launch campaign, and social media activation."
)

experience_2 = ExperienceTuple(
    id = 2,
    company = "QuattrGroup",
    start_date = datetime(2020, 5, 1),
    end_date = datetime(2022, 3, 15),
    position = "Director of Marketing, New Business Director, Member of the Investment Board",
    achievements = ACHIEVEMENTS_2,
    order = 2,
    )

ACHIEVEMENTS_3 = (
    "Developed research-driven communication strategies for clients across public, commercial, and state sectors, "
    "including Honda, Electrolux, OLX, Київстар, and PepsiCo. Projects included: the Dozorro platform, "
    "a national cybersecurity campaign for the National Police, communication support for the State Aid Reform, "
    "the SESAR project for the Antimonopoly Committee of Ukraine, and initiatives with the Kyiv City State Administration. "
    "Co-authored the national crisis communications concept in partnership with the Ministry of Information Policy "
    "and the National Security and Defense Council of Ukraine."
)

experience_3 = ExperienceTuple(
    id = 3,
    company = "RAM Group",
    start_date = datetime(2017, 9, 23),
    end_date = datetime(2020, 4, 12),
    position = "Strategic Director, Big Data Business Consultant, Analyst",
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
    soft_skill_text = (
        "Skilled at motivating others, developing clear and comprehensive briefs, "
        "providing constructive feedback, and ensuring task completion aligned with objectives. "
        "Experienced in managing analytics, creative, content, and SMM teams."
    ),
    )

soft_skill_2 = SoftSkillTuple(
    id = 2,
    soft_skill_text = (
        "Capable of working independently to develop complete products, "
        "while achieving even better results in collaborative team environments."
    ),
    )

soft_skill_3 = SoftSkillTuple(
    id = 3,
    soft_skill_text = (
        "I learn, therefore I am: committed to continuous self-education in coding, analytics, and strategic thinking."
    ),
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
    degree_title = (
        "Specialist in Practical Psychology and English Philology, with teaching qualification in World Literature"
    ),
    )

education_2 = EducationTuple(
    id = 2,
    institution = "Hryhoriy Skovoroda Institute of Philosophy, National Academy of Sciences of Ukraine",
    start_date = datetime(2005, 11, 1),
    end_date = datetime(2008, 7, 1),
    degree_title = (
        "Completed postgraduate studies in Philosophy with a focus on Ethics, Aesthetics, and Personality"
    ),
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

# natural language

natural_lang_1 = NaturalLangTuple(
    id = 1,
    natural_lang = "English",
    level = "ready to deliver interview",

    )

natural_lang_2 = NaturalLangTuple(
    id = 2,
    natural_lang = "Ukrainian",
    level = "fluent",

    )

natural_lang_3 = NaturalLangTuple(
    id = 3,
    natural_lang = "Russian",
    level = "fluent",

    )

natural_lang_4 = NaturalLangTuple(
    id = 4,
    natural_lang = "German",
    level = "basic",

    )

NATURAL_LANGS_ENG = [
    natural_lang_1,
    natural_lang_2,
    natural_lang_3,
    natural_lang_4,

    ]
