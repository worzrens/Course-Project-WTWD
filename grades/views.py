from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.db.models import Q

from grades.models import Pupil, Group, Grade
from grades.serializer import PupilSerializer, DetailedPupilSerializer, GroupSerializer, DetailedGroupSerializer, \
    GradeSerializer


class PupilViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return {
            'list': PupilSerializer,
            'retrieve': DetailedPupilSerializer,
        }.get(self.action, PupilSerializer)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return {
            'list': GroupSerializer,
            'retrieve': DetailedGroupSerializer,
        }.get(self.action, GroupSerializer)


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return {
            'list': GradeSerializer,
            'retrieve': GradeSerializer,
        }.get(self.action, GradeSerializer)


class FilteredGradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GradeSerializer

    def list(self, request):
        request_filters = request.query_params
        print(request_filters)

        filter_query = Q()
        for key, value in request_filters.items():
            filter_query.add(Q(**{key: value}), Q.AND)

        queryset = Grade.objects.filter(filter_query)
        serializer = GradeSerializer(queryset, many=True)
        return Response(serializer.data)

