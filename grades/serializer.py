from rest_framework import serializers
from grades.models import Pupil, Group
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


class DetailedPupilSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Pupil
        fields = ['first_name', 'last_name', 'patronymic', 'group']


class DetailedGroupSerializer(serializers.ModelSerializer):
    speciality = CustomChoiceField(choices=SCHOOL_SPECIALITY_CHOICES)
    pupils = PupilSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['year', 'speciality', 'pupils']
