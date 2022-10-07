import django.core.exceptions
import random

from datacenter.models import Chastisement, Commendation, Lesson, Mark, Schoolkid


COMMENDATIONS_SAMPLES = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!',
]


def get_schoolkid_by_name(schoolkid_name: str) -> Schoolkid:
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except django.core.exceptions.MultipleObjectsReturned:
        print(f'Multiple records for query {schoolkid_name}. Please clarify name.')
        return None
    except django.core.exceptions.ObjectDoesNotExist:
        print(f'No records found for query {schoolkid_name}.')
        return None
    return schoolkid


def fix_marks(schoolkid_name: str) -> None:
    schoolkid = get_schoolkid_by_name(schoolkid_name)
    if not schoolkid:
        return     
    Mark.objects.filter(schoolkid=schoolkid).filter(points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid_name: str) -> None:
    schoolkid = get_schoolkid_by_name(schoolkid_name)
    if not schoolkid:
        return     
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid_name: str, subject: str) -> None:
    schoolkid = get_schoolkid_by_name(schoolkid_name)
    if not schoolkid:
        return 
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study, 
        group_letter=schoolkid.group_letter, 
        subject__title__contains=subject
    ).order_by().reverse().first()
    if not lesson:
        print(f"Can't find lesson {subject}. Please clarify subject name.")
        return
    commendation_text = random.choice(COMMENDATIONS_SAMPLES)
    Commendation.objects.create(
        text=commendation_text, 
        subject=lesson.subject, 
        teacher=lesson.teacher, 
        schoolkid=schoolkid, 
        created=lesson.date
    )
