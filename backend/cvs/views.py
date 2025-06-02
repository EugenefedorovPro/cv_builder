import ipdb
from rest_framework.views import APIView
from rest_framework.response import Response
from cvs.serializers import (HeaderSerializer,
                             HardSkillSerializer, ManifestSerializer,
                             )
from cvs.models.models import (Header,
                               HardSkill,
                               BlockNames, Manifest,

                               )


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