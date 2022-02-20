class User:
    '''
    Class that generates new intances of Users
    '''
    user_list = []

    def __init__(self, username, password):
        '''
        Function that initializes the user
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_user method and user objects to user_list
        '''
        User.user_list.append(self)



    
