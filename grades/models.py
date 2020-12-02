from django.db import models
from django.db.models import Count

from grades.utils import SCHOOL_SPECIALITY_CHOICES


class Group(models.Model):
    year = models.IntegerField()
    speciality = models.CharField(max_length=2, choices=SCHOOL_SPECIALITY_CHOICES, default='LI')

    def get_pupils_count(self):
        return Pupil.objects.filter(group=self).count()

    def __str__(self):
        return "ID: %s | Y: %s | S: %s" % (self.pk, self.year, self.speciality)


class Pupil(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    group = models.ForeignKey(Group, related_name='pupils', on_delete=models.CASCADE)

    def get_own_grades(self):
        return Grade.objects.filter(pupil=self)


class Subject(models.Model):
    name = models.CharField(max_length=30)


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    subject = models.OneToOneField(Subject, related_name='teacher', on_delete=models.CASCADE)


class Grade(models.Model):
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField()
    mark = models.IntegerField()
