from django.shortcuts import render
from rest_framework.decorators import api_view
from models import Text

# Create your views here.
@api_view(["POST", "GET"])
def summarize(request):

    if request.method == "POST":
        return None