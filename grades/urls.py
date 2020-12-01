from django.urls import path, include
from rest_framework import routers

from grades.views import PupilViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'pupils', PupilViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
]