from sqlalchemy import and_


from .db import session
from .models import Student, Teacher, Group, Grade, Discipline


def get_all_students(st):
    pass


def get_all_teachers(user):
    pass


def get_all_disciplines(user):
    pass


def get_all_group():
    pass


def create_student(fullname, g_id):
    student = Student(fullname=fullname, group_id=g_id)
    session.add(student)
    session.commit()
    session.close()


def create_teacher(fullname):
    teacher = Teacher(fullname=fullname)
    session.add(teacher)
    session.commit()
    session.close()


def create_discipline(name, t_id):
    discipline = Discipline(name=name, teacher_id = t_id)
    session.add(discipline)
    session.commit()
    session.close()


def create_grade(grade, data, s_id, d_id):
    grade = Grade(grade=grade, date_of=data, student_id=s_id, discipline_id=d_id)
    session.add(grade)
    session.commit()
    session.close()


def create_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()
    session.close()


def update_student(_id, fullname, g_id):
    student = session.query(Student).filter(Student.id == _id)
    if student:
        student.update({"fullname": fullname, "group_id": g_id})
        session.commit()
    session.close()
    return student.first()


def update_teacher(_id, fullname):
    teacher = session.query(Teacher).filter(Teacher.id == _id)
    if teacher:
        teacher.update({"fullname": fullname})
        session.commit()
    session.close()
    return teacher.first()


def update_discipline(_id, name, t_id):
    discipline = session.query(Discipline).filter(Discipline.id == _id)
    if discipline:
        discipline.update({"name": name, "teacher.id": t_id})
        session.commit()
    session.close()
    return discipline.first()


def update_grade(grade, data, s_id, d_id):
    grade1 = session.query(Grade).filter(and_(Student.id == s_id, Discipline.id == d_id))
    if grade1:
        grade1.update({"grade": grade, "data": data})
        session.commit()
    session.close()
    return grade1.first()


def update_group(_id, name):
    group = session.query(Group).filter((Group.id == _id))
    if group:
        group.update({"name": name,})
        session.commit()
    session.close()
    return group.first()


def delete_student(_id):
    r = session.query(Student).filter(Student.id == _id).delete()
    session.commit()
    session.close()
    return r


def delete_teacher(_id):
    r = session.query(Teacher).filter(Teacher.id == _id).delete()
    session.commit()
    session.close()
    return r


def delete_discipline(_id):
    r = session.query(Discipline).filter(Discipline.id == _id).delete()
    session.commit()
    session.close()
    return r


def delete_group(_id):
    r = session.query(Group).filter(Group.id == _id).delete()
    session.commit()
    session.close()
    return r


def delete_grade(_id):
    r = session.query(Grade).filter(Grade.id == _id).delete()
    session.commit()
    session.close()
    return r
