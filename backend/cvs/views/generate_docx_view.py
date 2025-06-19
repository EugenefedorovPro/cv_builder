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


class GenerateDocx(APIView):
    def _fetch_photo(self, lang: str, doc: DocxTemplate):
        photo_url = str(Photos.objects.filter(lang__lang = lang).first().photo_url)
        photo_path = os.path.join(settings.MEDIA_ROOT, photo_url)
        img = Image.open(str(photo_path))
        clean_path = Path("/tmp/clean_quattr.jpg")
        img.convert("RGB").save(clean_path, format = "JPEG")
        photo = InlineImage(doc, str(clean_path), width = Mm(25))
        return photo

    def _fetch_manifest(self, lang: str) -> Manifest:
        manifest: Manifest = Manifest.objects.filter(lang__lang = lang).first()
        manifest_text = manifest.manifest_text if manifest else ""
        return manifest_text

    def _fetch_header(self, lang: str, doc: DocxTemplate) -> HeaderTuple:
        header: Header = Header.objects.filter(lang__lang = lang).first()

        email = RichText()
        email.add(
            header.email,
            url_id = doc.build_url_id(header.email),
            color = "0000FF",
            size = 18,
            font = "Verdana",
            )

        linkedin = RichText()
        linkedin.add(
            "linkedin",
            url_id = doc.build_url_id(header.linkedin),
            color = "0000FF",
            size = 18,
            font = "Verdana",
            )

        github = RichText()
        github.add(
            "github",
            url_id = doc.build_url_id(header.github),
            color = "0000FF",
            size = 18,
            font = "Verdana",
            )

        first_name = RichText()
        first_name.add(
            header.first_name.upper(),
            size = 24,
            font = "Verdana",
            bold = True,
            )

        second_name = RichText()
        second_name.add(
            header.second_name.upper(),
            size = 24,
            font = "Verdana",
            bold = True,
            )

        phone = RichText()
        phone.add(
            header.phone.upper(),
            size = 18,
            font = "Verdana",
            )

        country = RichText()
        country.add(
            header.country,
            size = 18,
            font = "Verdana",
            )

        city = RichText()
        city.add(
            header.city,
            size = 18,
            font = "Verdana",
            )

        district = RichText()
        district.add(
            header.district,
            size = 18,
            font = "Verdana",
            )

        header_tuple = HeaderTuple(
            first_name = first_name,
            second_name = second_name,
            phone = phone,
            email = email,
            linkedin = linkedin,
            github = github,
            country = country,
            city = city,
            district = district,

            )

        return header_tuple

    def _fetch_block_names(self, lang: str) -> BlockNameTuple:
        block_names: BlockNames = BlockNames.objects.filter(lang__lang = lang).first()
        font = "Verdana",
        size = 18

        country_title = RichText()
        country_title.add(
            block_names.country_title,
            font = font,
            size = size,
            bold = True,

            )

        city_title = RichText()
        city_title.add(
            block_names.city_title,
            font = font,
            size = size,
            bold = True,

            )

        district_title = RichText()
        district_title.add(
            block_names.district_title,
            font = font,
            size = size,
            bold = True,

            )

        hard_skills_name = RichText()
        hard_skills_name.add(
            block_names.hard_skills_name,
            font = font,
            size = 24,
            bold = True,

            )

        block_names_tuple = BlockNameTuple(
            country_title = country_title,
            city_title = city_title,
            district_title = district_title,
            hard_skills_name = hard_skills_name,

            )

        return block_names_tuple

    def _fetch_hard_skills(self, lang: str) -> list[dict[str, RichText | str]]:
        hard_skills_qs: QuerySet[HardSkill] = HardSkill.objects.filter(lang__lang = lang)
        hard_skills: list[dict[str, RichText | str]] = []
        for item in hard_skills_qs:
            hard_skills.append(
                {
                    "category": RichText(
                        item.category,
                        bold = True,
                        ),
                    "hard_skill_text": item.hard_skill_text,
                    }
                )

        return hard_skills


    def get(self, request):
        lang = request.GET.get("lang")
        template_path = Path(__file__).parent.parent / "doc_templates" / "cv.docx"
        doc = DocxTemplate(template_path)

        photo: Photos = self._fetch_photo(lang, doc)
        manifest_text: str = self._fetch_manifest(lang)
        header_tuple: HeaderTuple = self._fetch_header(lang, doc)
        block_names_tuple: BlockNameTuple = self._fetch_block_names(lang)
        hard_skills = self._fetch_hard_skills(lang)

        # ipdb.set_trace()
        context = {
            # photo
            "photo": photo,
            # header
            "first_name": header_tuple.first_name,
            "second_name": header_tuple.second_name,
            "phone": header_tuple.phone,
            "email": header_tuple.email,
            "linkedin": header_tuple.linkedin,
            "github": header_tuple.github,
            "country": header_tuple.country,
            "city": header_tuple.city,
            "district": header_tuple.district,
            "country_title": block_names_tuple.country_title,
            "city_title": block_names_tuple.city_title,
            "district_title": block_names_tuple.district_title,
            # manifest
            "manifest": manifest_text,
            # hard_skills
            "hard_skills_name": block_names_tuple.hard_skills_name,
            "hard_skills": hard_skills,

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
