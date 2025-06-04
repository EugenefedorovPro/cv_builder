from rest_framework import serializers
from cvs.models.models import (Header,
                               Photos,
                               HardSkill,
                               Manifest,
                               Project,
                               SoftSkill,
                               )


class PhotoSerializer(serializers.ModelSerializer):
    photo_url = serializers.ImageField()

    class Meta:
        model = Photos
        fields = ["photo_url"]


class HeaderSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer()

    class Meta:
        model = Header
        fields = ["id",
                  "photo",
                  "first_name",
                  "second_name",
                  "phone",
                  "email",
                  "linkedin",
                  "github",
                  "country",
                  "city",
                  "district",
                  ]


class HardSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardSkill
        fields = ["id", "category", "hard_skill_text"]


class ManifestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manifest
        fields = ["id", "manifest_text"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "project_name", "project_text", "web_url", "git_url"]


class SoftSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftSkill
        fields = ["id", "soft_skill_text"]
