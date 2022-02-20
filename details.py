import imp
import random
import string


class Details:
    '''
    Class that generates new instances of details
    '''
    user_details = [] # Empty details list

    def __init__(self, account_name ,user_name, user_password):

        # docstring removed for simplicity

        self.account_name = account_name
        self.user_name = user_name
        self.user_password = user_password

        # save_details function called upon on a details object and appends it to the details_list
        
    def save_details(self):
        '''
            save_details function saves details into user_details.
        '''

        Details.user_details.append(self)

        # delete_details function called upon on details object and removes it from the details_list

    def delete_details(self):
        '''
            Function to delete saved detail from the user_details.
        '''
        
        Details.user_details.remove(self)


    @classmethod
    def find_by_account_name(cls, account_name):
        '''
        A method that processes an inputted account_name and returns details that matches the account_name
        

        Args:
            account_name: account_name to search
        Return : 
            Details that matches the account_name
        '''

        for details in cls.user_details:
            if details.account_name == account_name:
                return details
        return False

    @classmethod
    def details_exist(cls, account_name):
        '''
        Method that checks if details exists from the user_details list.
        Args:
            account_name: account_name to search for if it exists
        Returns :
            Boolean: True or false depending if the user_details exists
        '''
        for details in cls.user_details:
            if details.account_name == account_name:
                return True
        return False

    @classmethod
    def display_details(cls):
        '''
        Method that returns and display details from user_details list
        '''
        return cls.user_details


    @classmethod
    def generate_password(cls, length):
        '''
          Method that lays a blueprint of what is required for a strong password and enables the user to generate a password for use in the new account.  
        '''
        passcode = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*<?>"

        return ''.join(random.choice(passcode) for i in range(length))
