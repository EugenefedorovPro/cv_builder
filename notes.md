Context:

    from collections import namedtuple
    ProjectTuple = namedtuple("ProjectTuple", ("project_name", "project_text", "web_url", "git_url"))

Example:

    project_1 = ProjectTuple(
        project_name = "Creative Website for Poetry",
        project_text = "A Django-based web application that generates random "
                       "verses from an original poetry corpus on each visit, "
                       "contrasting them with the author's curated works to explore"
                       " the boundary between randomness and deliberate expression. "
                       "Deployed with Docker, Nginx, and SSL.",
        web_url = "https://eupoetry.kyiv.ua/",
        git_url = "https://github.com/EugenefedorovPro/eu_poetry_website",

        )

Data:

    PROJECTS_ENG: dict[str, dict[str, str]] = {

        "Creative Website for Poetry": {
            "project_text": "A Django-based web application that generates random "
                            "verses from an original poetry corpus on each visit, "
                            "contrasting them with the author's curated works to explore"
                            " the boundary between randomness and deliberate expression. "
                            "Deployed with Docker, Nginx, and SSL.",
            "web_url": "https://eupoetry.kyiv.ua/",
            "git_url": "https://github.com/EugenefedorovPro/eu_poetry_website"

            },

        "App to Find Rhymes to a Word": {
            "project_text": "An open-source Python project and web application "
                            "that implements a custom rhyme theory to generate rhymes for Russian words "
                            "using NLP, machine learning (PyTorch-based neural networks for transcription "
                            "and stress detection), and optimized algorithms "
                            "(generator-based data processing, multiprocessing,"
                            " and OOP design patterns). Built with Django and deployed using Docker and Nginx.",
            "web_url": "http://rhyme.kyiv.ua/",
            "git_url": "https://github.com/EugenefedorovPro/rhyme_rus"

            },

        "NN to Put Stress onto a Word": {
            "project_text": "An open-source Python package that predicts the position of stress in any Russian word — "
                            "including neologisms — using a neural network trained on parsed Wiktionary data. "
                            "Built with TensorFlow/Keras and GRU layers, "
                            "and powered by custom preprocessing and IPA phonetic encoding.",
            "web_url": "",
            "git_url": "https://github.com/EugenefedorovPro/put_stress_rus",

            },


        "NN to Transcribe Words": {
            "project_text": "An open-source Python package that converts any Russian word — "
                            "including neologisms — into its International Phonetic Alphabet (IPA) transcription "
                            "using a GRU-based neural network with 99.96% categorical accuracy. "
                            "Built with TensorFlow/Keras and trained on a custom-parsed Russian Wiktionary dataset.",
            "web_url": "",
            "git_url": "https://github.com/EugenefedorovPro/word2ipa_rus",

            },

        "Poll-Making Forms Platform": {
            "project_text": "A web-based platform for creating and managing polls, "
                            "similar to Google Forms, using Django, JavaScript, and MySQL. "
                            "Implemented anonymous respondent tracking, "
                            "duplicate response prevention via browser fingerprinting, "
                            "and a custom admin panel with role-based access for poll creators and administrators. "
                            "Optimized analytics processing for large datasets (270,000 pings) using multiprocessing "
                            "and efficient ORM queries, reducing computation time from 7 to 2.3 seconds.",
            "web_url": "https://poll.eger.in.ua/",
            "git_url": "",

            },

        "Custom Monitoring System": {
            "project_text": "A real-time monitoring system, featuring asynchronous ping tracking, "
                            "sound alerts for missed pings, and dynamic charts using React (TypeScript) "
                            "for visualization. Leveraged Django with Redis for scalable backend processing and "
                            "MySql for persistent data storage. Optimized analytics queries to process 270,000 pings in 2.3 seconds, "
                            "with role-based access control for users and admins.",
            "web_url": "",
            "git_url": "",

            },

        "C Data Structures and Algorithms for Python": {
            "project_text": "Developed a library of algorithms and data structures "
                            "(red-black tree, hash table, sorting, linked list, queue) in C, "
                            "integrated as Python packages using Cython and Python’s C API.",
            "web_url": "",
            "git_url": "https://github.com/EugenefedorovPro/c_algorithms_for_python",

            },

        }
Rewrite the Data according to the Example:
