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


                               )
from django.db.models import QuerySet


class HeaderView(APIView):
    def get(self, request):
        header = Header.objects.all().first()
        serializer = HeaderSerializer(header)
        return Response(serializer.data)


class HardSkillView(APIView):
    def get(self, request):
        hard_skills = HardSkill.objects.all()
        serializer_hard_skills = HardSkillSerializer(hard_skills, many = True)
        hard_skills_name = BlockNames.objects.all().first().hard_skills_name
        block_name = {
            "block_name": hard_skills_name
            }

        return Response((block_name, serializer_hard_skills.data))


class ManifestView(APIView):
    def get(self, request):
        manifest: Manifest = Manifest.objects.all().first()
        serializer = ManifestSerializer(manifest)
        block_name = {
            "block_name": BlockNames.objects.all().first().manifest_name
            }
        return Response((block_name, serializer.data))


class ProjectView(APIView):
    def get(self, request):
        projects: QuerySet[Project] = Project.objects.all()
        serializer_project = ProjectSerializer(projects, many = True)
        block_name: dict[str, str] = {
            "block_name": BlockNames.objects.all().first().projects_name
            }
        return Response((block_name, serializer_project.data))


class ExperienceView(APIView):
    def get(self, request):
        experience_items: QuerySet[Experience] = Experience.objects.all()
        serializer_project = ExperienceSerializer(experience_items, many = True)
        block_name: dict[str, str] = {
            "block_name": BlockNames.objects.all().first().experience_name
            }
        return Response((block_name, serializer_project.data))


class SoftSkillView(APIView):
    def get(self, request):
        soft_skills: QuerySet[SoftSkill] = SoftSkill.objects.all()
        serializer_soft_skill = SoftSkillSerializer(soft_skills, many = True)
        block_name: dict[str, str] = {
            "block_name": BlockNames.objects.all().first().soft_skills_name
            }
        return Response((block_name, serializer_soft_skill.data))


class EducationView(APIView):
    def get(self, request):
        education_items: QuerySet[Education] = Education.objects.all()
        serializer_education = EducationSerializer(education_items, many = True)
        block_name: dict[str, str] = {
            "block_name": BlockNames.objects.all().first().education_name,
            }
        return Response((block_name, serializer_education.data))


class InterestView(APIView):
    def get(self, request):
        interest_items: QuerySet[Interest] = Interest.objects.all()
        serializer_interest = InterestSerializer(interest_items, many = True)
        block_name: dict[str, str] = {
            "block_name": BlockNames.objects.all().first().interest_name,
            }
        return Response((block_name, serializer_interest.data))
