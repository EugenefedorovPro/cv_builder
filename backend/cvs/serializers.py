from rest_framework import serializers
from cvs.models.models import (Header,
                               Photos,
                               HardSkill,
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


# class BlockNamesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BlockNames
#         fields = [
#             "header_name",
#             "hard_skills_name",
#             "manifest_name",
#             "projects_name",
#             "experience_name",
#             "soft_skills_name",
#             "education_name",
#             "hobby_name",
#             "cases_name",
#             "why_me_name",
#             ]


class HardSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardSkill
        fields = ["id", "category", "hard_skill_text"]
