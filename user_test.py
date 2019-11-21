import unittest  # Importing the unittest module
from user import User  # Importing class user

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.
    Args:
         unittest.TestCase:TestCase that help in creating test cases
    """
    def setUp(self):
        """
        set up method to run before each test cases.
        """
        
    def test_init(self):
        """
        checks to test if the object is initialized properly
        """

if __name__ == '__main__':
    unittest.main()