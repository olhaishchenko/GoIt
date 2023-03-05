from .db import session
from .db import Student
def get_all_students(st):

    return user


def get_all_teachers(user):


    return todos


def create_student(_id, name, model):
    student = Student(fullname=name, group_id=_id)
    session.add(student)
    session.commit()
    session.close()

def create_teacher(name, model):
    teacher = model(fullname=name)
    session.add(teacher)
    session.commit()
    session.close()

def create_discipline(_id, name, model):
    discipline = model(fullname=name, teacher_id = _id)
    session.add(discipline)
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