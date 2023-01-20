from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import Text

from summarizer.summary import *

# Create your views here.
@api_view(["POST", "GET"])
def summarize(request):

    if request.method == "POST":

        text = request.data["text"]

        new_addition = Text(text = text)
        new_addition.save()

        return Response(status = 200)

    else:

        latest = Text.objects.latest("time_sent")
        summary = summarize(latest)

        return summary