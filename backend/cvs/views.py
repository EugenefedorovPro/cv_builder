from html.parser import HTMLParser

from io import BytesIO
import ipdb
from rest_framework.views import APIView
from rest_framework.response import Response
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
from docxtpl import DocxTemplate
from pathlib import Path
from django.http import HttpResponse


class HeaderView(APIView):
    def get(self, request):
        lang = request.GET.get("lang")
        header = Header.objects.filter(lang__lang = lang).first()
        serializer = HeaderSerializer(header)
        return Response(serializer.data)


class HardSkillView(APIView):
    def get(self, request):
        lang = request.GET.get("lang")
        hard_skills = HardSkill.objects.filter(lang__lang = lang)
        serializer_hard_skills = HardSkillSerializer(hard_skills, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        block_name = {
            "block_name": block_names_ins.hard_skills_name if block_names_ins else None
            }

        return Response((block_name, serializer_hard_skills.data))


class ManifestView(APIView):
    def get(self, request):
        lang = request.GET.get("lang")
        manifest: Manifest = Manifest.objects.all().first()
        serializer = ManifestSerializer(manifest)
        block_names_ins: BlockNames = BlockNames.objects.all().filter(lang__lang = lang).first()
        block_name = {
            "block_name": block_names_ins.manifest_name if block_names_ins else None
            }
        return Response((block_name, serializer.data))


class ProjectView(APIView):
    def get(self, request):
        lang: str = request.GET.get("lang")
        projects: QuerySet[Project] = Project.objects.filter(lang__lang = lang)
        serializer_project = ProjectSerializer(projects, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        block_name = {
            "block_name": block_names_ins.projects_name if block_names_ins else None
            }
        return Response((block_name, serializer_project.data))


class ExperienceView(APIView):
    def get(self, request):
        lang: str = request.GET.get("lang")
        experience_items: QuerySet[Experience] = Experience.objects.filter(lang__lang = lang)
        serializer_project = ExperienceSerializer(experience_items, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        block_name = {
            "block_name": block_names_ins.experience_name if block_names_ins else None
            }
        return Response((block_name, serializer_project.data))


class SoftSkillView(APIView):
    def get(self, request):
        lang: str = request.GET.get("lang")
        soft_skills: QuerySet[SoftSkill] = SoftSkill.objects.filter(lang__lang = lang)
        serializer_soft_skill = SoftSkillSerializer(soft_skills, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        block_name = {
            "block_name": block_names_ins.soft_skills_name if block_names_ins else None
            }
        return Response((block_name, serializer_soft_skill.data))


class EducationView(APIView):
    def get(self, request):
        lang: str = request.GET.get("lang")
        education_items: QuerySet[Education] = Education.objects.filter(lang__lang = lang)
        serializer_education = EducationSerializer(education_items, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        block_name = {
            "block_name": block_names_ins.education_name if block_names_ins else None
            }
        return Response((block_name, serializer_education.data))


class InterestView(APIView):
    def get(self, request):
        lang: str = request.GET.get("lang")
        interest_items: QuerySet[Interest] = Interest.objects.filter(lang__lang = lang)
        serializer_interest = InterestSerializer(interest_items, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        block_name = {
            "block_name": block_names_ins.interest_name if block_names_ins else None
            }
        return Response((block_name, serializer_interest.data))


class NaturalLangView(APIView):
    def get(self, request):
        lang: str = request.GET.get("lang")
        natural_lang_items: QuerySet[NaturalLanguage] = NaturalLanguage.objects.filter(lang__lang = lang)
        serializer_natural_lang = NaturalLangSerializer(natural_lang_items, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        block_name = {
            "block_name": block_names_ins.natural_lang_name if block_names_ins else None
            }
        return Response((block_name, serializer_natural_lang.data))


class GenerateDocx(APIView):
    def get(self, request):
        template_path = Path(__file__).parent / "doc_templates" / "cv.docx"
        doc = DocxTemplate(template_path)
        manifest = Manifest.objects.first()
        manifest_text = manifest.manifest_text if manifest else ""

        context = {
            "manifest": manifest_text
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
