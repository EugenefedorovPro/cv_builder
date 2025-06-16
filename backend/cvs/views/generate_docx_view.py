from rest_framework.views import APIView
from html.parser import HTMLParser
from PIL import Image

from io import BytesIO
import ipdb
from docxtpl import (DocxTemplate,
                     InlineImage,
                     )
from docx.shared import Mm
from pathlib import Path
from django.http import HttpResponse
from cvs.serializers import (HeaderSerializer,
                             HardSkillSerializer,
                             ManifestSerializer,
                             ProjectSerializer,
                             SoftSkillSerializer,
                             EducationSerializer,
                             ExperienceSerializer,
                             InterestSerializer,
                             NaturalLangSerializer,
                             )
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

                               )
from django.db.models import QuerySet



class GenerateDocx(APIView):
    def get(self, request):
        lang = request.GET.get("lang")
        template_path = Path(__file__).parent.parent / "doc_templates" / "cv.docx"
        doc = DocxTemplate(template_path)

        photo_path = Path(__file__).parent.parent / "management" / "commands" / "quattr.jpg"
        img = Image.open(photo_path)
        clean_path = Path("/tmp/clean_quattr.jpg")
        img.convert("RGB").save(clean_path, format = "JPEG")

        photo = InlineImage(doc, str(clean_path), width = Mm(25))

        manifest = Manifest.objects.first()
        manifest_text = manifest.manifest_text if manifest else ""

        context = {
            "manifest": manifest_text,
            "photo": photo,

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
