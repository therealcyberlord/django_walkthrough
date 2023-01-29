from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Text

from summarizer.summary import *

# Create your views here.
@api_view(["POST"])
def summarize_view(request):

    if request.method == "POST":

        text = request.data["text"]

        new_addition = Text(text = text)
        new_addition.save()

        summary = summarize(new_addition.text)

        return Response(summary, status = 200)