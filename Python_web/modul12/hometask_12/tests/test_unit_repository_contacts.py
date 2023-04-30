import unittest
from datetime import date
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from src.database.models import Contact, User
from src.schemas import ContactModel
from src.repository.contacts import get_contacts, get_contact_by_id, get_contact_by_birthday, get_contacts_body_field, \
    create, update_contact, remove


class TestContactsRepository(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1, username='testname', email='testuser@gmail.com', password='password')

    async def test_get_contacts(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter().offset().limit().all.return_value = contacts
        result = await get_contacts(0, 10, self.user, self.session)
        self.assertEqual(result, contacts)

    async def test_create(self):
        body = ContactModel(
            first_name='Name',
            last_name='Familie',
            email='testemail@test.com',
            telephone_number='+30999999999',
            date_of_birthday=date(2010, 5, 1),
            # user_id=self.user.id,
        )
        result = await create(body, self.session)
        self.assertEqual(result.first_name, body.first_name)
        self.assertEqual(result.last_name, body.last_name)
        self.assertEqual(result.email, body.email)
        self.assertEqual(result.telephone_number, body.telephone_number)
        self.assertEqual(result.date_of_birthday, body.date_of_birthday)
        # self.assertEqual(result.user_id, body.user_id)
        self.assertTrue(hasattr(result, 'id'))

    async def test_get_contact_by_id(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter().first.return_value = contacts
        result = await get_contact_by_id(1, self.user, self.session)
        self.assertEqual(result, contacts)

    async def test_get_contacts_body_field(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query(Contact).filter().all.return_value = contacts
        result = await get_contacts_body_field('email', self.user.email, self.user, self.session)
        self.assertEqual(result, contacts)

    async def test_get_contact_by_birthday(self):
        contacts = [Contact(date_of_birthday=date(2010, 5, 1)), Contact(date_of_birthday=date(2010, 5, 2)),
                    Contact(date_of_birthday=date(2010, 5, 3))]
        self.session.query(Contact).all.return_value = contacts
        result = await get_contact_by_birthday(self.session)
        self.assertEqual(result, contacts)

    async def test_update_contact(self):
        contact = Contact(
            first_name='Myname',
            last_name='MyFamilie',
            email='myemail@test.com',
            telephone_number='+30888888888',
            date_of_birthday=date(2012, 4, 2),
        )
        body = ContactModel(
            first_name='Name',
            last_name='Familie',
            email='testemail@test.com',
            telephone_number='+30999999999',
            date_of_birthday=date(2010, 5, 1),
        )
        self.session.query().filter().first.return_value = contact
        result = await update_contact(1, self.user, body, self.session)
        self.assertEqual(result.first_name, body.first_name)
        self.assertEqual(result.last_name, body.last_name)
        self.assertEqual(result.email, body.email)
        self.assertEqual(result.telephone_number, body.telephone_number)
        self.assertEqual(result.date_of_birthday, body.date_of_birthday)

    async def test_remove(self):
        contact = Contact()
        self.session.query().filter().first.return_value = contact
        result = await remove(1, self.user, self.session)
        self.assertEqual(result, contact)


if __name__ == '__main__':
    unittest.main()
