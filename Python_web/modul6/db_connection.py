from psycopg2 import connect, Error
from contextlib import contextmanager


@contextmanager
def connection():
    conn = None
    try:
        conn = connect(host='raja.db.elephantsql.com', user='ikcoculc', database='ikcoculc', password='wiMLLPZd16N9Cm0FVYIUPCJkHlCmBXaZ')
        yield conn
        conn.commit()
    except Error as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()