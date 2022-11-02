from datetime import datetime, timedelta, date

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
    print(users)


def interval_week():
    day_today = datetime.today().date()
    day = timedelta(days=1)
    weeks = timedelta(weeks=1)
    begin_interval = day_today + day
    end_interval = day_today + weeks
    print(begin_interval, end_interval)
    return begin_interval, end_interval


def get_birthdays_per_week():
    (first_day, last_day) = interval_week()
    begin_week = first_day.timetuple().tm_yday
    end_week = last_day.timetuple().tm_yday
    week_birthday = {}
    for user in users:
        user['birthday'] = user['birthday'].replace(year=2022)
        if begin_week < user['birthday'].timetuple().tm_yday < end_week:
            week_birthday[user['birthday'].strftime('%A')] = user['name']
    user_Monday = []
    for user_birth_key, user_birth_value in week_birthday.items():
        if user_birth_key in ('Monday', 'Saturday', 'Sunday'):
            user_Monday.append(user_birth_value)
    week_birthday.pop(week_birthday['Monday'])
            # week_birthday.pop(user_birth_key)

        # week_birthday['Monday'] = user_Monday

    print(week_birthday)


    # print(first_day, last_day)

get_birthdays_per_week()

