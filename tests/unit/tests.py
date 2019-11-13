import os
import unittest

from app import app, dba
from app.models import User, Media, Comment

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        self.app =app.test_client()

    def tearDown(self):
        dba.session.remove()

    # Expectation
    # username = tester123
    # name = tester123
    def test_get_user(self):
        user = User.query.filter_by(username='tester123').first()
        assert user.name == 'tester123'

if __name__ == '__main__':
    unittest.main()