from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def myhome(request):
    return Response({
        "Messagessss":"this is myn first apis"
    })
