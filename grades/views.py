from rest_framework import viewsets
from grades.models import Pupil, Group
from grades.serializer import PupilSerializer, DetailedPupilSerializer, GroupSerializer, DetailedGroupSerializer


class PupilViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()

    def get_serializer_class(self):
        return {
            'list': PupilSerializer,
            'retrieve': DetailedPupilSerializer,
        }.get(self.action, PupilSerializer)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()

    def get_serializer_class(self):
        return {
            'list': GroupSerializer,
            'retrieve': DetailedGroupSerializer,
        }.get(self.action, GroupSerializer)

