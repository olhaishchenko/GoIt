from mongoengine import *

from connection_db import connection_string

connect(host=connection_string, ssl=True)


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = DateField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField()


class Quote(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()
