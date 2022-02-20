import unittest
from user import User


class TestUser(unittest.TestCase):
    '''
     Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Set up function for the test class to create a new user
        '''
        self.new_user = User("kchamdany", "45chamdany")

    def test_user_created(self):
        '''
        Function to test to find if the user object is created successfully
        '''
        self.assertEqual(self.new_user.username, "kchamdany")
        self.assertEqual(self.new_user.password, "45chamdany")


    def tearDown(self):
        '''
        tearDown method cleans up after each test case has run.
        '''
        User.user_list = []

 