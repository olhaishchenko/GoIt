import argparse
from sqlalchemy import and_
import sys
from sqlalchemy.exc import SQLAlchemyError

from src.crud import create_student, create_teacher, create_discipline

parser = argparse.ArgumentParser(description='Todo APP')
parser.add_argument('-a', '--action', choices=['create', 'read', 'update', 'delete'],  required=True)
parser.add_argument('-m', '--model', choices=['Group', 'Student', 'Teacher', 'Discipline', 'Grade'], required=True)
parser.add_argument('-d', '--data', required=True)
parser.add_argument("-fn", "--fullname", default=None)
parser.add_argument('-n', '--name', required=True, default=None)
parser.add_argument("-gid", "--group_id", default=None)
parser.add_argument("-tid", "--teacher_id", default=None)
parser.add_argument("-did", "--discipline_id", default=None)
parser.add_argument("-sid", "--student_id", default=None)
parser.add_argument('-g', '--grade', required=True)
parser.add_argument('--id')


arguments = parser.parse_args()
# print(arguments)
my_arg = vars(arguments)
# print(my_arg)

action = my_arg.get('action')
model = my_arg.get('model')
data = my_arg.get('data')
name = my_arg.get('name')
fullname = my_arg.get('fullname')
name = my_arg.get('name')
g_id = my_arg.get('group_id')
t_id = my_arg.get('teacher_id')
d_id = my_arg.get('discipline_id')
s_id = my_arg.get('student_id')
grade = my_arg.get('grade')
_id = my_arg.get('id')


def main(user):
    match action:
        case 'create':
            if model == 'Teacher':
                create_teacher(fullname=fullname)
            elif model == 'Student':
                create_student(fullname=fullname, g_id=g_id)
            elif model == 'Discipline':
                create_discipline(fullname=fullname, t_id = t_id)

        case 'list':
            todos = get_all_todos(user)
            for t in todos:
                print(t.id, t.title, t.description, t.user.login)
        case 'update':
            t = update_todo(_id=_id, title=title, description=description, user=user)
            if t:
                print(t.id, t.title, t.description, t.user.login)
            else:
                print('Not found')
        case 'remove':
            r = remove_todo(_id=_id, user=user)
            print(f'Remove: {r}')
        case _:
            print('Nothing')


if __name__ == '__main__':
    user = get_user(login)
    password = input('Password: ')
    if password == user.password:
        main(user)
    else:
        print('Password wrong!')