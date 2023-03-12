from mongoengine import *

# connect(host="mongodb+srv://userweb9:567234@cluster0.byupvtg.mongodb.net/web9?retryWrites=true&w=majority", ssl=True)
connect(host=f"mongodb://127.0.0.1:27017/web9")


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = DateField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField()


class Quote(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()
