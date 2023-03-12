from mongoengine import *

# connect(host="mongodb+srv://userweb9:567234@cluster0.byupvtg.mongodb.net/web9?retryWrites=true&w=majority", ssl=True)
connect(host=f"mongodb://127.0.0.1:27017/web9")


class Contact(Document):
    fullname = StringField(required=True, unique=True)
    email = DateField(max_length=50)
    age = IntField()
    phone_number = StringField()
    country = StringField()
    result = BooleanField(default=False)