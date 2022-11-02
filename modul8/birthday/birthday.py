from datetime import datetime, timedelta

users = []
with open('birthday.txt', 'r') as bh:
    while True:
        line = bh.readline()
        if not line:
            break
        line_birthday = line.strip().split(' ')
        user = {
            'name': line_birthday[0],
            'birthday': datetime.strptime(line_birthday[1], '%d.%m.%Y').date(),
            }
        users.append(user)


def get_birthdays_per_week():
    week_birthday = dict()
    week_birthday['Monday'] = []
    day_today = datetime.today().date()
    day = timedelta(days=1)
    begin_interval = day_today + day
    for i in range(7):
        for item in users:
            if begin_interval.strftime('%d') == item['birthday'].strftime('%d') and \
                    begin_interval.strftime('%m') == item['birthday'].strftime('%m'):
                if begin_interval.strftime('%A') not in week_birthday.keys():
                    if begin_interval.strftime('%A') not in ('Saturday', 'Sunday'):
                        week_birthday[begin_interval.strftime('%A')] = [item['name']]
                    else:
                        week_birthday['Monday'].append(item['name'])
                elif begin_interval.strftime('%A') not in ('Saturday', 'Sunday'):
                    week_birthday[begin_interval.strftime('%A')].append(item['name'])
        begin_interval += day
    return week_birthday


def print_birthday_per_week(dict_user):
    day_today = datetime.today().date()
    day = timedelta(days=1)
    begin_interval = day_today + day
    for i in range(7):
        if begin_interval.strftime('%A') in dict_user.keys():
            print(f'{begin_interval.strftime("%A")}: {", ".join(dict_user[begin_interval.strftime("%A")])}')
        begin_interval += day

print_birthday_per_week(get_birthdays_per_week())

