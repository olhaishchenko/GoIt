import pprint
from faker import Faker
from db_connection import connection

fake = Faker('uk-UA')
simple_select = """
    SELECT * FROM users WHERE id=%s 
"""

select = """
    SELECT id, name, email, age
    FROM users
    WHERE age>45
    ORDER BY name, age DESC
    LIMIT 10
"""

select_regex = """
    SELECT id, name, email, age
    FROM users
    WHERE name SIMILAR TO '%рій|ко%'
    ORDER BY name, age DESC
    LIMIT 10
"""
if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        # c.execute(simple_select)
        # print

        # c.execute(select)
        # print(c.fetchall())
        c.execute(select_regex)
        print(c.fetchall())
        c.close()
