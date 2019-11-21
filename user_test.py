import unittest 
from user import User  

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
        
    def test_save_object(self):
        """
        checks wether object is saved corectly
        """
        
    def tearDown(self):
        """
        tearDown method that does clear up after test case has run.
        """
        User.user_list = []
        
    
    
if __name__ == '__main__':
    unittest.main()