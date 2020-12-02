import os
from datetime import datetime
from random import choice, randint

import django


def populate():
    print('Starting population script...')
    # groups = [
    #     Group.objects.get_or_create(year=year, speciality=speciality[0])[0]
    #     for speciality in SCHOOL_SPECIALITY_CHOICES
    #     for year in range(10, 12)
    # ]
    #
    # FIRST_NAMES = ['Александр', 'Алексей', 'Анастасия', 'Анна', 'Артем', 'Виктория', 'Владислав', 'Даниил', 'Дарья', 'Дмитрий', 'Екатерина', 'Елизавета', 'Иван', 'Ксения', 'Максим', 'Мария', 'Михаил', 'Наталья', 'Никита', 'Павел', 'Полина', 'Сергей', 'Юлия']
    # LAST_NAMES = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов', 'Новиков', 'Фёдоров',]
    # PATRONYMICS = ['Алексеевич', 'Артёмович', 'Вадимович', 'Владимирович', 'Валентинович', 'Данильевич', 'Денисович', 'Дмитриевич', 'Егорович', 'Леонидович', 'Максимович', 'Матвевич', 'Олегович', 'Павлович',]
    #
    # pupils = [
    #     Pupil.objects.get_or_create(
    #         first_name=choice(FIRST_NAMES),
    #         last_name=choice(LAST_NAMES),
    #         patronymic=choice(PATRONYMICS),
    #         group=group)[0]
    #     for _ in range(2)
    #     for group in groups
    #     if group.get_pupils_count() < 6
    # ]

    subjects = [
        Subject.objects.get_or_create(name=name)[0]
        for name in ['Математика', 'Физика', 'Украинский язык', "Иностранный язык", "Программирование"]
    ]

    pupils = Pupil.objects.all()

    grades = [
        Grade.objects.get_or_create(
            pupil=pupil,
            subject=subject,
            date=datetime.now(),
            mark=randint(4, 12)
        )[0]
        for subject in subjects
        for pupil in pupils
    ]

    # print(f'Groups created {len(groups)}')
    print(f'Pupils created {len(pupils)}')
    print(f'Subjects created {len(subjects)}')
    print(f'Grades created {len(grades)}')
    print('Done!')


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
    django.setup()

    from grades.models import Group, Pupil, Subject, Grade
    from grades.utils import SCHOOL_SPECIALITY_CHOICES

    populate()
