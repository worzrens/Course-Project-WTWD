from rest_framework import serializers
from grades.models import Pupil, Group, Grade, Subject
from grades.utils import SCHOOL_SPECIALITY_CHOICES


class CustomChoiceField(serializers.ChoiceField):
    def to_representation(self, data):
        if data not in self.choices.keys():
            self.fail('invalid_choice', input=data)
        else:
            return self.choices[data]

    def to_internal_value(self, data):
        for key, value in self.choices.items():
            if value == data:
                return key
        self.fail('invalid_choice', input=data)


class GroupSerializer(serializers.ModelSerializer):
    speciality = CustomChoiceField(choices=SCHOOL_SPECIALITY_CHOICES)
    pupils_count = serializers.IntegerField(source='get_pupils_count')

    class Meta:
        model = Group
        fields = ['year', 'speciality', 'pupils_count']


class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = ['first_name', 'last_name', 'patronymic']


class DetailedGroupSerializer(serializers.ModelSerializer):
    speciality = CustomChoiceField(choices=SCHOOL_SPECIALITY_CHOICES)
    pupils = PupilSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['year', 'speciality', 'pupils']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']


class GradeSerializer(serializers.ModelSerializer):
    pupil = PupilSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Grade
        fields = ['pupil', 'subject', 'date', 'mark']


class SimpleGradeSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Grade
        fields = ['subject', 'date', 'mark']


class DetailedPupilSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    grades = SimpleGradeSerializer(many=True, source='get_own_grades')

    class Meta:
        model = Pupil
        fields = ['first_name', 'last_name', 'patronymic', 'group', 'grades']
