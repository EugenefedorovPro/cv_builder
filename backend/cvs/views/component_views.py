import ipdb
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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


class HeaderView(APIView):
    def get(self, request):
        lang = request.GET.get("lang")
        header = Header.objects.filter(lang__lang = lang).first()
        if not header:
            return Response(
                {
                    "details": f"No header data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {
                    "details": f"No block_names data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )
        block_name = {
            "github_title": block_names_ins.github_title,
            "linkedin_title": block_names_ins.linkedin_title,
            "country_title": block_names_ins.country_title,
            "city_title": block_names_ins.city_title,
            "district_title": block_names_ins.district_title,
            }
        serializer = HeaderSerializer(header)
        return Response(
            {
                "block_names": block_name,
                "header": serializer.data,
                }
            )


class HardSkillView(APIView):
    def get(self, request):
        lang = request.GET.get("lang")
        hard_skills = HardSkill.objects.filter(lang__lang = lang)
        if not hard_skills:
            return Response(
                {
                    "details": f"No hard_skills data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )
        serializer = HardSkillSerializer(hard_skills, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {
                    "details": f"No block_names data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )
        block_name = {
            "hard_skills_name": block_names_ins.hard_skills_name if block_names_ins else None
            }
        return Response(
            {
                "block_names": block_name,
                "hard_skills": serializer.data,
                }
            )


class ManifestView(APIView):
    def get(self, request):
        lang = request.GET.get("lang")
        manifest: Manifest = Manifest.objects.all().first()
        if not manifest:
            return Response(
                {
                    "details": f"No manifest data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )
        serializer = ManifestSerializer(manifest)
        block_names_ins: BlockNames = BlockNames.objects.all().filter(lang__lang = lang).first()
        if not block_names_ins:
            return Response(
                {
                    "details": f"No block_names data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )

        block_names = {
            "manifest_name": block_names_ins.manifest_name if block_names_ins else None
            }
        return Response(
            {
                "block_names": block_names,
                "manifest": serializer.data,
                }
            )


class ProjectView(APIView):
    def get(self, request):
        lang: str = request.GET.get("lang")
        projects: QuerySet[Project] = Project.objects.filter(lang__lang = lang)
        if not projects:
            return Response(
                {
                    "details": f"No projects data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )
        serializer = ProjectSerializer(projects, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {
                    "details": f"No block_names data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )
        block_names = {
            "project_name": block_names_ins.projects_name if block_names_ins else None
            }
        return Response({
            "block_names": block_names,
            "projects": serializer.data
            })


class ExperienceView(APIView):
    def get(self, request):
        lang: str = request.GET.get("lang")
        experience_qs: QuerySet[Experience] = Experience.objects.filter(lang__lang = lang)
        if not experience_qs:
            return Response(
                {
                    "details": f"No experience data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )
        serializer = ExperienceSerializer(experience_qs, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {
                    "details": f"No block_names data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )
        block_names = {
            "experience_name": block_names_ins.experience_name,
            "company_title": block_names_ins.company_title,
            "exp_period_title": block_names_ins.exp_period_title,
            "position_title": block_names_ins.position_title,
            'achievements_title': block_names_ins.achievements_title,
            }
        return Response(
            {
                "block_names": block_names,
                "experience": serializer.data
                },
            )


class SoftSkillView(APIView):
    def get(self, request):
        lang: str = request.GET.get("lang")
        soft_skills_qs: QuerySet[SoftSkill] = SoftSkill.objects.filter(lang__lang = lang)
        if not soft_skills_qs:
            return Response(
                {
                    "details": f"No soft_skills data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )

        serializer = SoftSkillSerializer(soft_skills_qs, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {
                    "details": f"No block_names data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )

        block_names = {
            "soft_skills_name": block_names_ins.soft_skills_name if block_names_ins else None
            }
        return Response(
            {
                "block_names": block_names,
                "soft_skills": serializer.data
                },
            )


class EducationView(APIView):
    def get(self, request):
        lang: str = request.GET.get("lang")
        education_qs: QuerySet[Education] = Education.objects.filter(lang__lang = lang)
        if not education_qs:
            return Response(
                {
                    "details": f"No education data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )
        serializer = EducationSerializer(education_qs, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {
                    "details": f"No block_names data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )

        block_names = {
            "education_name": block_names_ins.education_name if block_names_ins else None
            }

        return Response(
            {
                "block_names": block_names,
                "education": serializer.data
                },
            )


class InterestView(APIView):
    def get(self, request):
        lang: str = request.GET.get("lang")
        interest_qs: QuerySet[Interest] = Interest.objects.filter(lang__lang = lang)
        if not interest_qs:
            return Response(
                {
                    "details": f"No interest data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )
        serializer = InterestSerializer(interest_qs, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {
                    "details": f"No block_names data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )

        block_names = {
            "interest_name": block_names_ins.interest_name if block_names_ins else None
            }
        return Response(
            {
                "block_names": block_names,
                "interests": serializer.data
                },
            )


class NaturalLangView(APIView):
    def get(self, request):
        lang: str = request.GET.get("lang")
        natural_lang_qs: QuerySet[NaturalLanguage] = NaturalLanguage.objects.filter(lang__lang = lang)
        if not natural_lang_qs:
            return Response(
                {
                    "details": f"No natural languages data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )
        serializer = NaturalLangSerializer(natural_lang_qs, many = True)
        block_names_ins: BlockNames = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {
                    "details": f"No block_names data for language: {lang}"
                    },
                status = status.HTTP_404_NOT_FOUND,
                )
        block_names = {
            "natural_lang_name": block_names_ins.natural_lang_name if block_names_ins else None
            }
        return Response(
            {
                "block_names": block_names,
                "natural_langs": serializer.data
                },
            )
