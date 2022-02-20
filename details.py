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

        # save_details method called upon on a details object and appends it to the details_list
        
    def save_details(self):
        '''
            save_details function saves details into user_details.
        '''

        Details.user_details.append(self)