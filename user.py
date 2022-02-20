from distutils.log import error


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

    def delete_user(self):
        '''
        Function to delete user from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def user_exit(cls, username):
        '''
        Checks if entered username has an existing account in the user_list
        '''
        for user in cls.user_list:
            if user.username == username:
                return True
        return False

    @classmethod
    def find_user(cls, username):
        '''
        Checks if entered username has an existing account in the user_list and returns the username if it exists and an error if it doesn't exist
        '''
        for user in cls.user_list:
            if user.username == username:
                return user
        return error

    @classmethod
    def user_authentication(cls, username, password):
        '''
        Checks if inputted user information matches the information in the user_list
        '''
        user = cls.find_user(username)
        if user.username == username and user.password == password:
                return True
        return False
