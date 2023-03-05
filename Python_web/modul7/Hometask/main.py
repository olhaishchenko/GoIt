import argparse
from datetime import datetime


from src.crud import get_all_students, get_all_teachers, get_all_disciplines, get_all_group
from src.crud import create_student, create_teacher, create_discipline,create_group, create_grade
from src.crud import update_teacher,update_grade, update_group, update_discipline, update_student
from src.crud import delete_teacher, delete_discipline, delete_group, delete_student, delete_grade

parser = argparse.ArgumentParser(description='CRUD create read update delete')
parser.add_argument('-a', '--action', choices=['create', 'read', 'update', 'delete'],  required=True)
parser.add_argument('-m', '--model', choices=['Group', 'Student', 'Teacher', 'Discipline', 'Grade'], required=True)
parser.add_argument('-d', '--data', default=None)
parser.add_argument("-fn", "--fullname", default=None)
parser.add_argument('-n', '--name', default=None)
parser.add_argument("-gid", "--group_id", default=None)
parser.add_argument("-tid", "--teacher_id", default=None)
parser.add_argument("-did", "--discipline_id", default=None)
parser.add_argument("-sid", "--student_id", default=None)
parser.add_argument('-g', '--grade', default=None)
parser.add_argument('--id')


arguments = parser.parse_args()
# print(arguments)
my_arg = vars(arguments)
# print(my_arg)

action = my_arg.get('action')
model = my_arg.get('model')
data = my_arg.get('data')
fullname = my_arg.get('fullname')
name = my_arg.get('name')
g_id = my_arg.get('group_id')
t_id = my_arg.get('teacher_id')
d_id = my_arg.get('discipline_id')
s_id = my_arg.get('student_id')
grade = my_arg.get('grade')
_id = my_arg.get('id')


def main():
    match action:
        case 'create':
            if model == 'Teacher':
                create_teacher(fullname=fullname)
            elif model == 'Student':
                create_student(fullname=fullname, g_id=g_id)
            elif model == 'Discipline':
                create_discipline(name=name, t_id=t_id)
            elif model == 'Group':
                create_group(name=name)
            elif model == 'Grade':
                create_grade(grade=grade, data=datetime.strptime(data,'%Y-%M-%d').date(), s_id=s_id, d_id=d_id)
        case 'read':
            if model == 'Teacher':
                teachers = get_all_teachers()
                for teacher in teachers:
                    print(teacher.id, teacher.fullname)
            elif model == 'Student':
                students = get_all_students()
                for student in students:
                    print(student.id, student.fullname, 'group_id: ', student.group_id)
            elif model == 'Discipline':
                disciplines = get_all_disciplines()
                for discipline in disciplines:
                    print(discipline.id, discipline.name, 'teacher_id: ', discipline.teacher_id)
            elif model == 'Group':
                groups = get_all_group()
                for group in groups:
                    print(group.id, group.name)
            elif model == 'Grade':
                print('Impossible')
        case 'update':
            if model == 'Teacher':
                t = update_teacher(_id=_id, fullname=fullname)
                if t:
                    print(t.id, t.fullname)
                else:
                    print('Not found')
            elif model == 'Student':
                t = update_student(_id=_id, fullname=fullname, g_id=g_id)
                if t:
                    print(t.id, t.fullname, t.group_id)
                else:
                    print('Not found')
            elif model == 'Discipline':
                t = update_discipline(_id=_id, name=name, t_id=t_id)
                if t:
                    print(t.id, t.name, t.teacher_id)
                else:
                    print('Not found')
            elif model == 'Group':
                t = update_group(_id=_id, name=name)
                if t:
                    print(t.id, t.name)
                else:
                    print('Not found')
            elif model == 'Grade':
                t = update_grade(grade=grade, data=datetime.strptime(data,'%Y-%M-%d').date(), s_id=s_id, d_id=d_id)
                if t:
                    print(t.grade, t.data, t.student_id, t.discipline_id)
                else:
                    print('Not found')
        case 'delete':
            if model == 'Teacher':
                r = delete_teacher(_id=_id)
            elif model == 'Student':
                r = delete_student(_id=_id)
            elif model == 'Discipline':
                r = delete_discipline(_id=_id)
            elif model == 'Group':
                r = delete_group(_id=_id)
            elif model == 'Grade':
                r = delete_grade(_id=_id)
            print(f'Delete: {r}')
        case _:
            print('Nothing')


if __name__ == '__main__':
    main()
