from rest_framework import serializers
from cvs.models.models import Header


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ["id", "first_name", "second_name", "phone", "email", "linkedin", "github", "country", "city", "district", "photo"]
