from django.shortcuts import render
from rest_framework import viewsets
from .models import cafe_info
from .serializers import cafe_infoSerializer
# Create your views here.

class cafe_infoViewSet(viewsets.ModelViewSet):
    queryset = cafe_info.objects.all()
    serializer_class = cafe_infoSerializer