from sqlalchemy import func, desc, select, and_

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session


def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    """
    result = session.query(Student.fullname,
                            func.round(func.avg(Grade.grade), 2)\
                           .label('avg_grade')) \
        .select_from(Grade).join(Student)\
        .group_by(Student.id)\
        .order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2(discipline_id):
    """
    Знайти студента із найвищим середнім балом з певного предмета.
    :param discipline_id:
    """
    result = session.query(Discipline.name, Student.fullname,
                           func.round(func.avg(Grade.grade), 2)\
                           .label('avg_grade'))\
        .select_from(Grade).join(Student).join(Discipline)\
        .filter(Discipline.id == discipline_id)\
        .group_by(Student.id, Discipline.name)\
        .order_by(desc('avg_grade')).limit(1).all()
    return result


def select_3(discipline_id):
    """
    Знайти середній бал у групах з певного предмета.
    :param discipline_id:
    """
    result = session.query(Discipline.name, Group.name,
                           func.round(func.avg(Grade.grade), 2)\
                           .label('avg_grade'))\
        .select_from(Grade).join(Student).join(Discipline).join(Group)\
        .filter(Discipline.id == discipline_id)\
        .group_by(Group.name, Discipline.name)\
        .order_by(desc('avg_grade')).all()
    return result


def select_4(discipline_id):
    """
    найти середній бал на потоці (по всій таблиці оцінок) з певного предмета.
    :param discipline_id:
    """
    result = session.query(Discipline.name,
                           func.round(func.avg(Grade.grade), 2)\
                           .label('avg_grade'))\
        .select_from(Grade).join(Discipline) \
        .group_by(Discipline.name) \
        .filter(Discipline.id == discipline_id).all()
    return result


def select_5(teacher_id):
    """
    Знайти які курси читає певний викладач.
    :param teacher_id:
    """
    result = session.query(Discipline.name, Teacher.fullname)\
        .select_from(Discipline).join(Teacher)\
        .filter(Teacher.id == teacher_id).all()
    return result


def select_6(group_id):
    """
    Знайти список студентів у певній групі.
    :param group_id:
    """
    result = session.query(Student.fullname, Group.name)\
        .select_from(Student)\
        .join(Group)\
        .filter(Group.id == group_id).all()
    return result


def select_7(discipline_id, group_id):
    """
    Знайти оцінки студентів у окремій групі з певного предмета.
    :param discipline_id:
    :param group_id:
    """
    result = session.query(Student.fullname, Discipline.name, Group.name, Grade.grade)\
        .select_from(Grade).join(Discipline).join(Student).join(Group)\
        .filter(and_(Discipline.id == discipline_id, Group.id == group_id))\
        .order_by(Student.fullname).all()
    return result


def select_8(teacher_id):
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    :param teacher_id:
    """
    result = session.query(Teacher.fullname, Discipline.name,
                           func.round(func.avg(Grade.grade), 2)\
                           .label('avg_grade'))\
        .select_from(Grade).join(Discipline).join(Teacher)\
        .filter(Teacher.id == teacher_id) \
        .group_by(Teacher.fullname, Discipline.name) \
        .order_by(desc('avg_grade')).all()
    return result


def select_9(student_id):
    """
    Знайти список курсів, які відвідує певний студент.
    :param student_id:
    """
    result = session.query(Student.fullname, Discipline.name)\
        .select_from(Grade).join(Discipline).join(Student)\
        .filter(Student.id == student_id)\
        .group_by(Discipline.name, Student.fullname)\
        .order_by(Discipline.name).all()
    return result


def select_10(student_id, teacher_id):
    """
    Список курсів, які певному студенту читає певний викладач.
    :param student_id:
    :param teacher_id:
    :return:
    """
    result = session.query(Student.fullname, Teacher.fullname, Discipline.name)\
        .select_from(Grade).join(Discipline).join(Teacher).join(Student)\
        .filter(and_(Student.id == student_id, Teacher.id == teacher_id))\
        .group_by(Discipline.name, Student.fullname, Teacher.fullname)\
        .order_by(Discipline.name).all()
    return result

def select_11(teacher_id, student_id):
    """
    Середній бал, який певний викладач ставить певному студентові.
    :param teacher_id:
    :param student_id:
    """
    result = session.query(Teacher.fullname, Student.fullname, Discipline.name,
                           func.round(func.avg(Grade.grade), 2)\
                           .label('avg_grade'))\
        .select_from(Grade).join(Discipline).join(Teacher).join(Student)\
        .filter(and_(Teacher.id == teacher_id, Student.id == student_id))\
        .group_by(Teacher.fullname, Student.fullname, Discipline.name)\
        .order_by(Teacher.fullname).all()
    return result


def select_12(discipline_id, group_id):
    """
    Оцінки студентів у певній групі з певного предмета на останньому занятті.
    :param discipline_id:
    :param group_id:
    """
    subquery = (select(Grade.date_of).join(Discipline).where(
        and_(Grade.discipline_id == discipline_id, Group.id == group_id)
    ).order_by(desc(Grade.date_of)).limit(1).scalar_subquery())

    result = session.query(Discipline.name,
                      Student.fullname,
                      Group.name,
                      Grade.date_of,
                      Grade.grade
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group)\
        .filter(and_(Discipline.id == discipline_id, Group.id == group_id, Grade.date_of == subquery)) \
        .order_by(desc(Grade.date_of)) \
        .all()
    return result


if __name__ == '__main__':
    # print(select_1())
    # print(select_2(2))
    # print(select_3(2))
    # print(select_4(1))
    # print(select_5(1))
    # print(select_6(1))
    # print(select_7(1, 2))
    # print(select_8(1))
    # print(select_9(1))
    # print(select_10(1, 1))
    print(select_11(1, 1))
    # print(select_12(1, 2))