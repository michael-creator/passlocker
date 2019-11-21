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
        save_object test case to test if the object will be saved in user list and credential list
        """
    def tearDown(self):
        """
        tear down method that does clears up after test case has run.
        """
        
        Credential.credential_list = []
      def test_delete_credentials(self):
        """
        checks if the user can delete his or her credentials
        """
        self.new_credential.save_credential()
        test_credential = Credential("mickey", "instragram", "2017")
        test_credential.save_credential()
        self.new_credential.delete_credentials() 
        
    def test_find_credential_by_name(self):
        """
        test to check if we can find a user by using  account name and display information
        """
        self.new_credential.save_credential()
        test_credential = Credential("mickey", "facebook", "password")
        test_credential.save_credential()
        found_credential = Credential.find_by_name("facebook")
        self.assertEqual(found_credential.account_password, "password")
    
    def test_credential_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the account name
        """
        self.new_credential.save_credential()
        test_credential = Credential("mickey", "facebook", "password")
        test_credential.save_credential()
        credential_exist = Credential.credential_exists("facebook")
        self.assertTrue(credential_exist)
        
    def test_display_all_credential(self):
        '''
        method that return all the credential saved
        '''
        self.assertEqual(Credential.display_credentials(),
                         Credential.credentials_list)
  
if __name__ == '__main__':
    unittest.main()