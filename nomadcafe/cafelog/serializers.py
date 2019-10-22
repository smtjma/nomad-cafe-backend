from rest_framework import serializers
from cafelog.models import cafe_info

class cafe_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = cafe_info
        fields = '__all__'
        