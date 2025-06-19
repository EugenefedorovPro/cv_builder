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
from cvs.types import (HeaderTuple,
                       BlockNameTuple,
                       )


FONT_TEXT = "Lato",
SIZE_NAME = 28
SIZE_HEADER = 18
SISE_BODY = 24


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
                        size = SISE_BODY,

                        ),
                    "hard_skill_text": RichText(
                        text = item.hard_skill_text,
                        size = SISE_BODY,

                        )
                    }
                )

        return hard_skills

    def _fetch_experience(self, lang: str):
        experienc_qs: QuerySet[Experience] = Experience.objects.filter(lang__lang = lang)
        experience: list[dict[str, RichText]] = []



    def get(self, request):
        lang = request.GET.get("lang")
        template_path = Path(__file__).parent.parent / "doc_templates" / "cv.docx"
        doc = DocxTemplate(template_path)

        photo: Photos = self._fetch_photo(lang, doc)
        manifest: RichText = self._fetch_manifest(lang)
        header: dict[str, RichText] = self._fetch_header(lang, doc)
        block_names: dict[str, RichText] = self._fetch_block_names(lang)
        hard_skills: list[dict[str, RichText]] = self._fetch_hard_skills(lang)
        experiences = self._fetch_experience(lang)

        # ipdb.set_trace()
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
            "experiences": experiences,

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
