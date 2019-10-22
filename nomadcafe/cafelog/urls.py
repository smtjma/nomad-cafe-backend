from django.urls import path, include

from cafelog import views
from rest_framework import routers
router = routers.SimpleRouter()
router.register('cafeinfo', views.CafeinfoViewSet)

app_name = 'cafelog'
urlpatterns = [
    path('cafeinfo', include(router.urls)),
]