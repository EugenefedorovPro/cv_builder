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
    def _fetch_photo(self, lang: str, doc: DocxTemplate):
        photo_url = str(Photos.objects.filter(lang__lang = lang).first().photo_url)
        photo_path = os.path.join(settings.MEDIA_ROOT, photo_url)
        img = Image.open(str(photo_path))
        clean_path = Path("/tmp/clean_quattr.jpg")
        img.convert("RGB").save(clean_path, format = "JPEG")
        photo = InlineImage(doc, str(clean_path), width = Mm(25))
        return photo

    def _fetch_manifest(self, lang: str) -> RichText:
        manifest_qs: Manifest = Manifest.objects.filter(lang__lang = lang).first()
        manifest = RichText(
            text = manifest_qs.manifest_text,
            size = SIZE_HEADER,
            font = FONT_TEXT,
            )

        return manifest

    def _fetch_header(self, lang: str, doc: DocxTemplate) -> dict[str, RichText]:
        header_qs: Header = Header.objects.filter(lang__lang = lang).first()
        header_names: list[str] = [item.name for item in header_qs._meta.fields]

        headers: dict[str, RichText] = {}
        for name in header_names:
            if "email" in name:
                value = getattr(header_qs, name)
                headers[name] = RichText(
                    text = value,
                    url_id = doc.build_url_id(value),
                    color = "0000FF",
                    size = SIZE_HEADER,
                    font = FONT_TEXT,
                    )

            elif "linkedin" in name or "github" in name:
                value = getattr(header_qs, name)
                headers[name] = RichText(
                    text = name,
                    url_id = doc.build_url_id(value),
                    color = "0000FF",
                    size = SIZE_HEADER,
                    font = FONT_TEXT,
                    )
            else:
                value = getattr(header_qs, name)
                headers[name] = RichText(
                    text = value,
                    size = SIZE_HEADER,
                    font = FONT_TEXT,
                    bold = True,
                    )
        return headers


    def _fetch_block_names(self, lang: str) -> dict[str, RichText]:
        block_names_qs: BlockNames = BlockNames.objects.filter(lang__lang = lang).first()

        field_names: list[str] = [item.name for item in block_names_qs._meta.fields]

        block_names: dict[str, RichText] = {}
        for name in field_names:
            if "country" in name or "city" in name or "district" in name:
                block_names[name] = RichText(
                    text = getattr(block_names_qs, name),
                    font = FONT_TEXT,
                    size = SIZE_HEADER,
                    bold = True,
                    )
            elif "current" in name:
                block_names[name] = RichText(
                    text = getattr(block_names_qs, name),
                    font = FONT_TEXT,
                    size = SIZE_BODY,
                    )
            elif "title" in name:
                block_names[name] = RichText(
                    text = getattr(block_names_qs, name),
                    font = FONT_TEXT,
                    size = SIZE_BODY,
                    bold = True,
                    )
            else:
                block_names[name] = RichText(
                    text = getattr(block_names_qs, name),
                    font = FONT_TEXT,
                    size = SIZE_NAME,
                    bold = True,
                    )
        return block_names

    def _fetch_hard_skills(self, lang: str) -> list[dict[str, RichText]]:
        hard_skills_qs: QuerySet[HardSkill] = HardSkill.objects.filter(lang__lang = lang)
        hard_skills: list[dict[str, RichText | str]] = []
        for item in hard_skills_qs:
            hard_skills.append(
                {
                    "category": RichText(
                        item.category,
                        bold = True,
                        size = SIZE_BODY,

                        ),
                    "hard_skill_text": RichText(
                        text = item.hard_skill_text,
                        size = SIZE_BODY,

                        )
                    }
                )

        return hard_skills

    def _rich_exp(self, text: str) -> RichText:
        rich: RichText = RichText(
            text = text,
            font = FONT_TEXT,
            size = SIZE_BODY,
            )
        return rich


    def _fetch_experience(self, lang: str, current: str):
        experience_qs: QuerySet[Experience] = Experience.objects.filter(lang__lang = lang)
        experience: list[dict[str, RichText]] = []
        for item in experience_qs:
            experience.append(
                {
                    "company": RichText(text = item.company, font = FONT_TEXT, size = SIZE_BODY, bold = True),
                    "start_date": self._rich_exp(item.start_date.strftime(DATE_FORMATTER)),
                    "end_date": self._rich_exp(item.end_date.strftime(DATE_FORMATTER)) if item.end_date else current,
                    "position": self._rich_exp(item.position),
                    "achievements": self._rich_exp(item.achievements),

                    },
                )
        return experience

    def _rich_proj(self, text: str) -> RichText:
        return RichText(
            text = text,
            font = FONT_TEXT,
            size = SIZE_BODY,
            )

    def _rich_proj_url(self, name:str, url: str, doc: DocxTemplate) -> RichText:
        return RichText(
            text = name,
            url_id = doc.build_url_id(url),
            color = "0000FF",
            font = FONT_TEXT,
            size = SIZE_BODY,
            )

    def _fetch_projects(self, lang: str, doc: DocxTemplate) -> list[dict[str, RichText]]:
        projects_qs: QuerySet[Project] = Project.objects.filter(lang__lang = lang)
        projects: list[dict[str, RichText]] = []
        for item in projects_qs:
            projects.append(
                {
                    "project_name": RichText(text = item.project_name, font = FONT_TEXT, size = SIZE_BODY, bold = True),
                    "project_text": self._rich_proj(item.project_text),
                    "web_url": self._rich_proj_url("web", item.web_url, doc) if item.web_url else "",
                    "git_url": self._rich_proj_url("git", item.git_url, doc) if item.git_url else "",
                    }
                )
        return projects


    def get(self, request):
        lang = request.GET.get("lang")
        template_path = Path(__file__).parent.parent / "doc_templates" / "cv.docx"
        doc = DocxTemplate(template_path)

        block_names: dict[str, RichText] = self._fetch_block_names(lang)
        photo: Photos = self._fetch_photo(lang, doc)
        manifest: RichText = self._fetch_manifest(lang)
        header: dict[str, RichText] = self._fetch_header(lang, doc)
        hard_skills: list[dict[str, RichText]] = self._fetch_hard_skills(lang)
        experience = self._fetch_experience(lang, block_names["current"])
        projects = self._fetch_projects(lang, doc)

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
