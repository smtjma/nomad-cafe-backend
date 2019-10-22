from django.shortcuts import render
from rest_framework import viewsets
from .models import Cafeinfo
from .serializers import CafeinfoSerializer
# Create your views here.

class CafeinfoViewSet(viewsets.ModelViewSet):
    queryset = Cafeinfo.objects.all()
    serializer_class = CafeinfoSerializer