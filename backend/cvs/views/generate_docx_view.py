import os
from rest_framework.views import APIView
from PIL import Image

from io import BytesIO
import ipdb
from docxtpl import (DocxTemplate,
                     InlineImage,
                     RichText,
                     )
from docx.shared import Mm
from pathlib import Path
from django.http import HttpResponse
from cvs.models.models import (Header,
                               HardSkill,
                               BlockNames,
                               Manifest,
                               Project,
                               SoftSkill,
                               Education,
                               Experience,
                               Interest,
                               NaturalLanguage,
                               Photos,

                               )
from django.db.models import QuerySet
from django.conf import settings
from cvs.types import DATE_FORMATTER


FONT_TEXT = "Lato"
SIZE_NAME = 28
SIZE_HEADER = 18
SIZE_BODY = 24


class GenerateDocx(APIView):
    def _rich_header_normal(self, text: str) -> RichText:
        return RichText(
            text = text,
            font = FONT_TEXT,
            size = SIZE_HEADER,

            )

    def _rich_header_bold(self, text: str) -> RichText:
        return RichText(
            text = text,
            font = FONT_TEXT,
            size = SIZE_HEADER,
            bold = True,

            )

    def _rich_header_url(self, value, name: str, doc: DocxTemplate, is_text_value: bool = True) -> RichText:
        return RichText(
            text = value if is_text_value else name,
            url_id = doc.build_url_id(value),
            color = "0000FF",
            size = SIZE_HEADER,
            font = FONT_TEXT,

            )

    def _rich_body_normal(self, text: str) -> RichText:
        return RichText(
            text = text,
            font = FONT_TEXT,
            size = SIZE_BODY,

            )

    def _rich_body_bold(self, text: str) -> RichText:
        return RichText(
            text = text,
            font = FONT_TEXT,
            size = SIZE_BODY,
            bold = True,

            )

    def _rich_body_name(self, text: str) -> RichText:
        return RichText(
            text = text,
            font = FONT_TEXT,
            size = SIZE_NAME,
            bold = True,

            )

    def _rich_body_url(self, value: str, name: str, doc: DocxTemplate, is_text_value: bool = True) -> RichText:
        return RichText(
            text = value if is_text_value else name,
            url_id = doc.build_url_id(value),
            color = "0000FF",
            size = SIZE_BODY,
            font = FONT_TEXT,

            )

    def _fetch_photo(self, lang: str, doc: DocxTemplate):
        photo_url = str(Photos.objects.filter(lang__lang = lang).first().photo_url)
        photo_path = os.path.join(settings.MEDIA_ROOT, photo_url)
        img = Image.open(str(photo_path))
        clean_path = Path("/tmp/clean_quattr.jpg")
        img.convert("RGB").save(clean_path, format = "JPEG")
        return InlineImage(doc, str(clean_path), width = Mm(25))

    def _fetch_manifest(self, lang: str) -> RichText:
        manifest_obj: Manifest = Manifest.objects.filter(lang__lang = lang).first()
        return self._rich_header_normal(manifest_obj.manifest_text)

    def _fetch_header(self, lang: str, doc: DocxTemplate) -> dict[str, RichText]:
        header_obj: Header = Header.objects.filter(lang__lang = lang).first()
        header_names: list[str] = [item.name for item in header_obj._meta.fields]

        headers: dict[str, RichText] = {}
        for name in header_names:
            if "email" in name:
                value = getattr(header_obj, name)
                headers[name] = self._rich_header_url(value, name, doc, is_text_value = True)

            elif "linkedin" in name or "github" in name:
                value = getattr(header_obj, name)
                headers[name] = self._rich_header_url(value, name, doc, is_text_value = False)
            else:
                value = getattr(header_obj, name)
                headers[name] = self._rich_header_normal(value)
        return headers


    def _fetch_block_names(self, lang: str) -> dict[str, RichText]:
        block_names_obj: BlockNames = BlockNames.objects.filter(lang__lang = lang).first()

        field_names: list[str] = [item.name for item in block_names_obj._meta.fields]

        block_names: dict[str, RichText] = {}
        for name in field_names:
            if "country" in name or "city" in name or "district" in name:
                value = getattr(block_names_obj, name)
                block_names[name] = self._rich_header_bold(value)
            elif "current" in name:
                value = getattr(block_names_obj, name)
                block_names[name] = self._rich_header_normal(value)
            elif "title" in name:
                value = getattr(block_names_obj, name)
                block_names[name] = self._rich_body_bold(value)
            else:
                value = getattr(block_names_obj, name)
                block_names[name] = self._rich_body_name(value)
        return block_names

    def _fetch_hard_skills(self, lang: str) -> list[dict[str, RichText]]:
        hard_skills_qs: QuerySet[HardSkill] = HardSkill.objects.filter(lang__lang = lang)
        hard_skills: list[dict[str, RichText | str]] = []
        for item in hard_skills_qs:
            hard_skills.append(
                {
                    "category": self._rich_body_bold(item.category),
                    "hard_skill_text": self._rich_body_normal(item.hard_skill_text),

                    }
                )

        return hard_skills


    def _fetch_experience(self, lang: str, current: str):
        experience_qs: QuerySet[Experience] = Experience.objects.filter(lang__lang = lang)
        experience: list[dict[str, RichText]] = []
        for item in experience_qs:
            experience.append(
                {
                    "company": self._rich_body_bold(item.company),
                    "start_date": self._rich_body_normal(item.start_date.strftime(DATE_FORMATTER)),
                    "end_date": self._rich_body_normal(item.end_date.strftime(DATE_FORMATTER)) if item.end_date else current,
                    "position": self._rich_body_normal(item.position),
                    "achievements": self._rich_body_normal(item.achievements),

                    },
                )
        return experience

    def _fetch_projects(self, lang: str, doc: DocxTemplate) -> list[dict[str, RichText]]:
        projects_qs: QuerySet[Project] = Project.objects.filter(lang__lang = lang)
        projects: list[dict[str, RichText]] = []
        for item in projects_qs:
            projects.append(
                {
                    "project_name": self._rich_body_bold(item.project_name),
                    "project_text": self._rich_body_normal(item.project_text),
                    "web_url": self._rich_body_url("web", item.web_url, doc) if item.web_url else "",
                    "git_url": self._rich_body_url("git", item.git_url, doc) if item.git_url else "",
                    }
                )
        return projects

    def _fetch_soft_skills(self, lang: str) -> list[dict[str, RichText]]:
        soft_skills_qs: QuerySet[SoftSkill] = SoftSkill.objects.filter(lang__lang = lang)
        soft_skills: list[dict[str, RichText | str]] = []
        for item in soft_skills_qs:
            soft_skills.append(
                {
                    "soft_skill_text": self._rich_body_normal(item.soft_skill_text),

                    }
                )

        return soft_skills

    def _fetch_education(self, lang: str, current: str):
        education_qs: QuerySet[Education] = Education.objects.filter(lang__lang = lang)
        education: list[dict[str, RichText]] = []
        for item in education_qs:
            education.append(
                {
                    "institution": self._rich_body_bold(item.institution),
                    "start_date": self._rich_body_normal(item.start_date.strftime(DATE_FORMATTER)),
                    "end_date": self._rich_body_normal(item.end_date.strftime(DATE_FORMATTER)) if item.end_date else current,
                    "degree_title": self._rich_body_normal(item.degree_title),
                    },
                )
        return education

    def _fetch_natural_lang(self, lang: str) -> list[dict[str, RichText]]:
        natural_lang_qs: QuerySet[NaturalLanguage] = NaturalLanguage.objects.filter(lang__lang = lang)
        natural_lang: list[dict[str, RichText]] = []
        for item in natural_lang_qs:
            natural_lang.append(
                {
                    "natural_lang": self._rich_body_bold(item.natural_lang),
                    "level": self._rich_body_normal(item.level),

                    },
                )
        return natural_lang

    def _fetch_interest(self, lang: str) -> list[dict[str, RichText]]:
        interest_qs: QuerySet[Interest] = Interest.objects.filter(lang__lang = lang)
        interests: list[dict[str, RichText]] = []
        for item in interest_qs:
            interests.append(
                {
                    "interest_text": self._rich_body_normal(item.interest_text),
                    },
                )
        return interests

    def get(self, request):
        lang = request.GET.get("lang")
        template_path = Path(__file__).parent.parent / "doc_templates" / "cv.docx"
        doc = DocxTemplate(template_path)

        block_names: dict[str, RichText] = self._fetch_block_names(lang)
        current = block_names["current"]
        photo: Photos = self._fetch_photo(lang, doc)
        manifest: RichText = self._fetch_manifest(lang)
        header: dict[str, RichText] = self._fetch_header(lang, doc)
        hard_skills: list[dict[str, RichText]] = self._fetch_hard_skills(lang)
        experience = self._fetch_experience(lang, current)
        projects = self._fetch_projects(lang, doc)
        soft_skills = self._fetch_soft_skills(lang)
        education = self._fetch_education(lang, current)
        natural_langs = self._fetch_natural_lang(lang)
        interests = self._fetch_interest(lang)

        context = {
            # photo
            "photo": photo,
            # header
            "first_name": header["first_name"],
            "second_name": header["second_name"],
            "phone": header["phone"],
            "email": header["email"],
            "linkedin": header["linkedin"],
            "github": header["github"],
            "country": header["country"],
            "city": header["city"],
            "district": header["district"],
            "country_title": block_names["country_title"],
            "city_title": block_names["city_title"],
            "district_title": block_names["district_title"],
            # manifest
            "manifest": manifest,
            # hard_skills
            "hard_skills_name": block_names["hard_skills_name"],
            "hard_skills": hard_skills,
            # experiences
            "experience_name": block_names["experience_name"],
            "exp_period_title": block_names["exp_period_title"],
            "position_title": block_names["position_title"],
            "achievements_title": block_names["achievements_title"],
            "experience": experience,
            # projects
            "projects_name": block_names["projects_name"],
            "projects": projects,
            # soft sills
            "soft_skills_name": block_names["soft_skills_name"],
            "soft_skills": soft_skills,
            # education
            "education_name": block_names["education_name"],
            "ed_period_title": block_names["ed_period_title"],
            "degree_title": block_names["degree_title"],
            "education": education,
            # natural languages
            "natural_lang_name": block_names["natural_lang_name"],
            "natural_langs": natural_langs,
            # interests
            "interest_name": block_names["interest_name"],
            "interests": interests,

            }

        doc.render(context)

        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        response = HttpResponse(
            buffer.read(),
            content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        response['Content-Disposition'] = 'attachment; filename="cv.docx"'
        return response
