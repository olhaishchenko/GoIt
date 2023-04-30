import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session
from src.database.models import User
from src.schemas import UserModel
from src.repository.users import get_user_by_email, create_user, confirmed_email, update_avatar, update_token


class TestUsersRepository(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)

    async def test_create_user(self):
        body = UserModel(
            username = 'names',
            email = 'name@test.ua',
            password = 'secret'
        )
        result = await create_user(body, self.session)
        self.assertEqual(result.username, body.username)
        self.assertEqual(result.email, body.email)
        self.assertEqual(result.password, body.password)
        self.assertTrue(hasattr(result, 'id'))

    async def test_get_user_by_email(self):
        users = [User(email='test@test.ua'), User(), User()]
        self.session.query().filter_by().first.return_value = users
        result = await get_user_by_email('test@test.ua', self.session)
        self.assertEqual(result, users)

    async def test_get_user_by_email_not_found(self):
        self.session.query().filter_by().first.return_value = None
        result = await get_user_by_email('test1@test.ua', self.session)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
