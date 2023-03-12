

import random
from faker import Faker
from modul7.modul7_2.src.db import session
from modul7.modul7_2.src.models import Teacher, Student, TeacherStudent

fake = Faker()


def create_relationship():
    students = session.query(Student).all()
    teachers = session.query(Teacher).all()

    for student in students:
        teacher = random.choice(teachers)
        rel = TeacherStudent(teacher_id=teacher.id, student_id=student.id)
        session.add(rel)
    session.commit()


if __name__ == '__main__':
    create_relationship()