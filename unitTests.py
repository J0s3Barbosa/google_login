import unittest
import os

class UnitTests(unittest.TestCase):

    def test_getUser_from_env(self):
        user_login =  os.getenv('USER_LOGIN')
        assert user_login is not None
 


if __name__ == '__main__':
    unittest.main()
