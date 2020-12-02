from django.urls import path, include
from rest_framework import routers

from grades.views import PupilViewSet, GroupViewSet, GradeViewSet

router = routers.DefaultRouter()
router.register(r'pupils', PupilViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'grades', GradeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]