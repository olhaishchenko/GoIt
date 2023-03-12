from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.sql import select

engine = create_engine("sqlite:///:memory", echo=False)#True щоб все бачити
metadata= MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('fullname', String)
              )

addresses = Table('addresses', metadata,
              Column('id', Integer, primary_key=True),
              Column('email', String, nullable=False),
              Column('user_id', Integer, ForeignKey('users.id'))
              )

metadata.create_all(engine)

if __name__ == '__main__':
    with engine.connect() as conn:
        r_user = users.insert().values(fullname='Mykola Gryshyn')
        print(r_user)
        result_user = conn.execute(r_user)
        print(result_user.lastrowid)

        u = conn.execute(select(users))
        # print(u.fetchone())
        # print(u.all())

        r_address = addresses.insert().values(email='mykola@i.ua', user_id=result_user.lastrowid)
        conn.execute(r_address)
        a = conn.execute(select(addresses))
        print(a.fetchall())
        a_u = select(users.c.fullname, addresses.c.email).select_from(addresses).join(users).group_by(users.c.fullname)
        result = conn.execute(a_u)
        print(result.fetchall())
