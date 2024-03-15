from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from APIS.serializer import toolserializers
from APIS.models import apitool

# Create your views here.
@api_view(["GET"])
def mytools(request):
    alltools=apitool.objects.all().order_by("-id")
    mydata=toolserializers(alltools,many=True)
    return Response({
        "message":"data fetch successfully",
        "data":mydata.data
    })
