from typing import cast

import ipdb
from django.db.models import QuerySet
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from cvs.models.models import (
    BlockNames,
    CustomUser,
    Education,
    Experience,
    HardSkill,
    Header,
    Interest,
    Manifest,
    NaturalLanguage,
    Project,
    SoftSkill,
)
from cvs.serializers import (
    CustomUserSerializer,
    EducationSerializer,
    ExperienceSerializer,
    HardSkillSerializer,
    HeaderSerializer,
    InterestSerializer,
    ManifestSerializer,
    NaturalLangSerializer,
    ProjectSerializer,
    SoftSkillSerializer,
)
from cvs.types import (
    CustomUserType,
    EducationBlockNamesType,
    EducationData,
    EducationViewResponseType,
    ExperienceBlockNamesType,
    ExperienceData,
    ExperienceViewResponseType,
    HardSkillBlockNamesType,
    HardSkillData,
    HardSkillViewResponseType,
    HeaderBlockNamesType,
    HeaderData,
    HeaderViewResponseType,
    InterestBlockNamesType,
    InterestData,
    InterestViewResponseType,
    ManifestBlockNamesType,
    ManifestData,
    ManifestViewResponseType,
    NaturalLangBlockNamesType,
    NaturalLanguageData,
    NaturalLangViewResponseType,
    ProjectBlockNamesType,
    ProjectData,
    ProjectViewResponseType,
    SoftSkillBlockNamesType,
    SoftSkillData,
    SoftSkillViewResponseType,
    UserResponseType,
)


class UserView(APIView):
    def get(self, request: Request) -> Response:
        user_obj: CustomUser | None = CustomUser.objects.first()
        user_data: CustomUserType = cast(
            CustomUserType, CustomUserSerializer(user_obj).data
        )
        data: UserResponseType = {"user_data": user_data}
        return Response(data)


class HeaderView(APIView):
    def get(self, request: Request) -> Response:
        lang: str | None = request.GET.get("lang")
        header: Header | None = Header.objects.filter(lang__lang=lang).first()
        if not header:
            return Response(
                {"details": f"No header data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        block_names_ins: BlockNames | None = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {"details": f"No block_names data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        block_name: HeaderBlockNamesType = {
            "github_title": block_names_ins.github_title,
            "linkedin_title": block_names_ins.linkedin_title,
            "country_title": block_names_ins.country_title,
            "city_title": block_names_ins.city_title,
            "district_title": block_names_ins.district_title,
        }
        serializer = HeaderSerializer(header)
        header_data: HeaderData = cast(HeaderData, serializer.data)
        data: HeaderViewResponseType = {
            "block_names": block_name,
            "header": header_data,
        }
        return Response(data=data)


class HardSkillView(APIView):
    def get(self, request: Request) -> Response:
        lang = request.GET.get("lang")
        hard_skills: QuerySet[HardSkill] = HardSkill.objects.filter(lang__lang=lang)
        if not hard_skills:
            return Response(
                {"details": f"No hard_skills data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        hard_skills_data: list[HardSkillData] = cast(
            list[HardSkillData], HardSkillSerializer(hard_skills, many=True).data
        )
        block_names_ins: BlockNames | None = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {"details": f"No block_names data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        block_name: HardSkillBlockNamesType = {
            "hard_skills_name": (
                block_names_ins.hard_skills_name if block_names_ins else None
            )
        }
        hard_skill_response: HardSkillViewResponseType = {
            "block_names": block_name,
            "hard_skills": hard_skills_data,
        }
        return Response(hard_skill_response)


class ManifestView(APIView):
    def get(self, request: Request) -> Response:
        lang: str | None = request.GET.get("lang")
        manifest: Manifest | None = Manifest.objects.all().first()
        if not manifest:
            return Response(
                {"details": f"No manifest data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        manifest_data: ManifestData = cast(
            ManifestData, ManifestSerializer(manifest).data
        )
        block_names_ins: BlockNames | None = (
            BlockNames.objects.all().filter(lang__lang=lang).first()
        )

        if not block_names_ins:
            return Response(
                {"details": f"No block_names data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )

        block_names: ManifestBlockNamesType = {
            "manifest_name": block_names_ins.manifest_name if block_names_ins else None
        }
        manifest_response: ManifestViewResponseType = {
            "block_names": block_names,
            "manifest": manifest_data,
        }
        return Response(manifest_response)


class ProjectView(APIView):
    def get(self, request: Request) -> Response:
        lang: str | None = request.GET.get("lang")
        projects: QuerySet[Project] = Project.objects.filter(lang__lang=lang)
        if not projects:
            return Response(
                {"details": f"No projects data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        project_data: list[ProjectData] = cast(
            list[ProjectData], ProjectSerializer(projects, many=True).data
        )
        block_names_ins: BlockNames | None = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {"details": f"No block_names data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        block_names: ProjectBlockNamesType = {
            "project_name": block_names_ins.projects_name if block_names_ins else None
        }
        project_response: ProjectViewResponseType = {
            "block_names": block_names,
            "projects": project_data,
        }
        return Response(project_response)


class ExperienceView(APIView):
    def get(self, request: Request) -> Response:
        lang: str | None = request.GET.get("lang")
        experience_qs: QuerySet[Experience] | None = Experience.objects.filter(
            lang__lang=lang
        )
        if not experience_qs:
            return Response(
                {"details": f"No experience data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        experience_data: list[ExperienceData] = cast(
            list[ExperienceData], ExperienceSerializer(experience_qs, many=True).data
        )
        block_names_ins: BlockNames | None = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {"details": f"No block_names data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        block_names: ExperienceBlockNamesType = {
            "experience_name": block_names_ins.experience_name,
            "company_title": block_names_ins.company_title,
            "exp_period_title": block_names_ins.exp_period_title,
            "position_title": block_names_ins.position_title,
            "achievements_title": block_names_ins.achievements_title,
        }
        experience_response: ExperienceViewResponseType = {
            "block_names": block_names,
            "experience": experience_data,
        }
        return Response(experience_response)


class SoftSkillView(APIView):
    def get(self, request: Request) -> Response:
        lang: str | None = request.GET.get("lang")
        soft_skills_qs: QuerySet[SoftSkill] | None = SoftSkill.objects.filter(
            lang__lang=lang
        )
        if not soft_skills_qs:
            return Response(
                {"details": f"No soft_skills data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )

        soft_skills_data: list[SoftSkillData] = cast(
            list[SoftSkillData], SoftSkillSerializer(soft_skills_qs, many=True).data
        )
        block_names_ins: BlockNames = cast(BlockNames, BlockNames.objects.all().first())
        if not block_names_ins:
            return Response(
                {"details": f"No block_names data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )

        block_names: SoftSkillBlockNamesType = {
            "soft_skills_name": (
                block_names_ins.soft_skills_name if block_names_ins else None
            )
        }
        soft_skill_response: SoftSkillViewResponseType = {
            "block_names": block_names,
            "soft_skills": soft_skills_data,
        }
        return Response(soft_skill_response)


class EducationView(APIView):
    def get(self, request: Request) -> Response:
        lang: str | None = request.GET.get("lang")
        education_qs: QuerySet[Education] | None = Education.objects.filter(
            lang__lang=lang
        )
        if not education_qs:
            return Response(
                {"details": f"No education data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        education_data: list[EducationData] = cast(
            list[EducationData], EducationSerializer(education_qs, many=True).data
        )
        block_names_ins: BlockNames | None = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {"details": f"No block_names data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )

        block_names: EducationBlockNamesType = {
            "education_name": (
                block_names_ins.education_name if block_names_ins else None
            )
        }

        education_response: EducationViewResponseType = {
            "block_names": block_names,
            "education": education_data,
        }

        return Response(education_response)


class InterestView(APIView):
    def get(self, request: Request) -> Response:
        lang: str | None = request.GET.get("lang")
        interest_qs: QuerySet[Interest] | None = Interest.objects.filter(
            lang__lang=lang
        )
        if not interest_qs:
            return Response(
                {"details": f"No interest data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        interest_data: list[InterestData] = cast(
            list[InterestData], InterestSerializer(interest_qs, many=True).data
        )
        block_names_ins: BlockNames | None = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {"details": f"No block_names data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )

        block_names: InterestBlockNamesType = {
            "interest_name": block_names_ins.interest_name if block_names_ins else None
        }

        interest_response: InterestViewResponseType = {
            "block_names": block_names,
            "interests": interest_data,
        }
        return Response(interest_response)


class NaturalLangView(APIView):
    def get(self, request: Request) -> Response:
        lang: str | None = request.GET.get("lang")
        natural_lang_qs: QuerySet[NaturalLanguage] | None = (
            NaturalLanguage.objects.filter(lang__lang=lang)
        )
        if not natural_lang_qs:
            return Response(
                {"details": f"No natural languages data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        natural_lang_data: list[NaturalLanguageData] = cast(
            list[NaturalLanguageData],
            NaturalLangSerializer(natural_lang_qs, many=True).data,
        )
        block_names_ins: BlockNames | None = BlockNames.objects.all().first()
        if not block_names_ins:
            return Response(
                {"details": f"No block_names data for language: {lang}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        block_names: NaturalLangBlockNamesType = {
            "natural_lang_name": (
                block_names_ins.natural_lang_name if block_names_ins else None
            )
        }

        natural_lang_response: NaturalLangViewResponseType = {
            "block_names": block_names,
            "natural_langs": natural_lang_data,
        }
        return Response(natural_lang_response)
