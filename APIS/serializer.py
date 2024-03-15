from rest_framework import serializers
from APIS.models import apitool

class toolserializers(serializers.ModelSerializer):
    class Meta():
        model=apitool
        fields="__all__"