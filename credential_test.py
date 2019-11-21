import unittest  # Importing the unittest module
from credentials import Credential
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
        # self.new_user = User("mickey", "2019")
        self.new_credential = Credential("mickey", "facebook", "password")
   
if __name__ == '__main__':
    unittest.main()