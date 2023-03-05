from .db import session
from .models import Student, Teacher, Group, Grade, Discipline


def get_all_students(st):

    return user


def get_all_teachers(user):

    return todos


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

def create_discipline(fullname, t_id):
    discipline = Discipline(fullname=fullname, teacher_id = t_id)
    session.add(discipline)
    session.commit()
    session.close()

def create_grade(grade, data, s_id, d_id):
    grade = Grade(grade=grade, data=data, student_id=s_id, discipline_id=d_id)
    session.add(grade)
    session.commit()
    session.close()

def create_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()
    session.close()


def update_todo(_id, title, description, user):
    todo = session.query(Todo).filter(and_(Todo.user == user, Todo.id == _id))
    if todo:
        todo.update({"title": title, "description": description})
        session.commit()
    session.close()
    return todo.first()


def remove_todo(_id, user):
    r = session.query(Todo).filter(and_(Todo.user == user, Todo.id == id)).delete()
    session.commit()
    session.close()
    return r