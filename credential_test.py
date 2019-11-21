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
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.account_name, "facebook")
        self.assertEqual(self.new_credential.account_password, "password")
    def test_save_object(self):
        """
        save_object test case to test if the object will be save in user list and credential list
        """
    def tearDown(self):
        """
        tear down method that does clears up after test case has run.
        """
        
        Credential.credential_list = []
    
  
if __name__ == '__main__':
    unittest.main()