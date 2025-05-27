from django.http import HttpResponse
from django.urls import (path,
                         )

app_name = "cvs"

urlpatterns = [
    path("", HttpResponse("Placeholder for root django view")),

    ]
