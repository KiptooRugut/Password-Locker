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
        self.new_details = Details("Instagrtam", "Miguel", "Limits454")
        
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