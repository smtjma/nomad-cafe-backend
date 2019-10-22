from rest_framework import serializers
from cafelog.models import Cafeinfo

class CafeinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafeinfo
        fields = '__all__'
        