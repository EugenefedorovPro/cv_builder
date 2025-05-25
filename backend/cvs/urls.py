from django.http import HttpResponse
from django.urls import (path,
                         )

app_name = "cvs"


def stub(request):
    return HttpResponse("Placeholder for root django view")


urlpatterns = [
    path("", stub),

    ]
