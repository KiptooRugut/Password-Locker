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

     #Test case for saving our user
    def test_user_save(self):
        '''
        Function to find if the user object is saved to the user list.
        '''
        self.assertEqual(len(User.user_list), 0)
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_delete_user(self):
        '''
        Function to check if a user can be deleted from the user list.
        '''
        self.assertEqual(len(User.user_list), 0)
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 0)

    def test_find_user(self):
        '''
        test if the user account exists in the user list
        '''
        self.found_user = User.find_user("kchamdany")


    def test_user_exists(self):
        '''
        Function to test the user account exists in the user list
        '''
        self.found_user = User.user_exist("kchamdany")


if __name__ == '__main__':
    unittest.main()

