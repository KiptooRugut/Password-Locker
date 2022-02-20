import unittest  #Importing unittest module
from details import Details  #Importing the details class 


class TestDetails(unittest.TestCase):
    '''
    Test class that defines test cases for the details class behaviours.
    Args:
         unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Set up method to run testing each test cases
        '''
        self.new_details = Details("Instagram", "Miguel", "Limits454")
        
    def test_init(self):
        '''
            test_init test case checks if the details object has been created.
        '''
        self.assertEqual(self.new_details.account_socialmedia, "Instagram")
        self.assertEqual(self.new_details.user_name, "Miguel")
        self.assertEqual(self.new_details.user_password, "Limits454")

    def tearDown(self):
        '''
            tearDown method cleans up after each test case has run.
        '''
        Details.user_details = []
        

    def test_save_details(self):

        '''
        test_save_details test case, test to ascertain if the details object is saved into the user_details
        '''
        self.assertEqual(len(Details.user_details), 0)
        self.new_details.save_details()
        self.assertEqual(len(Details.user_details),1)


    def test_save_multiple_details(self):
            '''
            test_save_multiple_details to check if we can save multiple credential
            objects to our user_details
            '''
            self.new_details.save_details()
            test_details = Details("Test","user_name","Limits454") 
            test_details.save_details()
            self.assertEqual(len(Details.user_details),2)


    def test_delete_details(self):
            '''
            test if we can remove details from our user_details list
            '''
            self.assertEqual(len(Details.user_details), 0)
            self.new_details.save_details()
            self.assertEqual(len(Details.user_details), 1)
            self.new_details.delete_details()
            self.assertEqual(len(Details.user_details), 0)


    def test_find_details_by_account_socialmedia(self):
        '''
        test to check if we can find details by accout_socialmedia and display
        '''

        self.found_details = Details.find_by_account_socialmedia("Instagram")

    def test_details_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find user details.
        '''

        self.new_details.save_details()
        test_details = Details("Test","user_name","Limits454")
        test_details.save_details()

        details_exists = Details.details_exist("Test")

        self.assertTrue(details_exists)


    def test_display_all_details(self):
        '''
        method that returns a list of all details saved
        '''

        self.assertEqual(Details.display_details(),Details.user_details)




if __name__ == '__main__':
    unittest.main()

    