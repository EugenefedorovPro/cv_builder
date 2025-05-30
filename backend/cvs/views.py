from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HeaderSerializer
from cvs.models.models import Header

class HeaderView(APIView):
    def get(self, request):
        header = Header.objects.all().first()
        serializer = HeaderSerializer(header)
        return Response(serializer.data)