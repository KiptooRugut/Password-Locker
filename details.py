class Details():
    '''
    Class that generates new instances of details
    '''
    user_details = [] # Empty details list

    def __init__(self, account_name ,user_name, user_password):

        # docstring removed for simplicity

        self.account_name = account_name
        self.user_name = user_name
        self.user_password = user_password