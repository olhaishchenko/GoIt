from mongoengine import *

connect(host=f"mongodb+srv://userweb9:567234@cluster0.byupvtg.mongodb.net/?retryWrites=true&w=majority")

class Contact(Document):
    fullname = StringField(required=True, unique=True)
    email = StringField(max_length=50)
    age = IntField()
    phone_number = StringField()
    country = StringField()
    result = BooleanField(default=False)