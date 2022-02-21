#!/usr/bin/env python3.8
from user import User
from details import Details

def function():
	print("             ____                             _                                                        ")
	print("            |  _ \                           | |                                                       ")
	print("            | |_) )  ____    ___    ___      | |       ____       ____    _   _      ___     ______    ")
	print("            |  __/  / _  \  / __|  / __|     | |      /  _  \    /  __|  | | / /   ((___))  | |  ) )   ")
	print("            | |    / (_|  \ \  \__  \ \__    | |___   | (_)  |  |  |___  | |/\ \   ((___))  | |_) )    ")
	print("            |_|    \_____ / /___ /   /___/   |_____)   \____/    \_____| |_|  \_\  ((____   |_|  \_\   ")
function()


def create_new_user(user_name,user_password):
    """
    function that creates a new user
    """
    new_user = User(user_name,user_password) 
    return new_user
    
def generate_password(n):
    '''
    Function to facilitates creation of a strong password
    '''
    return Details.generate_password(n)


def save_user(user):
    """
    function that saves a new user
    """
    user.save_user()

def create_details(account_socialmedia,user_name,user_password):
    '''
    Function to create a new details
    '''
    new_details = Details(account_socialmedia,user_name,user_password)
    return new_details

def user_authentication(user_name,user_password):
    '''
    test that checks for user in the user_details array and authenticate the details information
    '''
    return User.user_authentication(user_name,user_password)

def save_details(details):
    """
    function to save details
    """ 
    details.save_details()

def display_details():
    '''
    Function that displays all saved details
    '''
    return Details.display_details()


def check_existing_details(account_socialmedia):
    '''
    Checks if inputted details exists with account_socialmedia, user_name and user_password and returns a Boolean
    '''
    return Details.details_exist(account_socialmedia)
    
def find_details(account_socialmedia):
    '''
    Function that finds details by account_socialmedia and returns the details
    '''
    return Details.find_by_account_socialmedia(account_socialmedia)

def del_details(details):
    '''
    Function to delete detail
    '''
    details.delete_details()



#main function
def main():
    print("Hello Welcome to your password locker!Please, Proceed to create your account")
    print("\n")
    
    print("Create account")
    print('-' * 50)
    print("Username")
    created_user_name = input()
    print("password")
    created_user_password = input()
    
    save_user(create_new_user(created_user_name,created_user_password))
    print("-"*50)
    print(f"Hello {created_user_name}, Account created succesfully! Your password is: {created_user_password}")
    print("\n")
    print("Proceed to login")
    print("-"*50)
    print("user_name")
    entered_user_name=input()
    print("-"*50)
    print("Your user_password")
    entered_user_password=input()
    print("-"*50)
    print("\n")
    if user_authentication(entered_user_name,entered_user_password):
        print(f"Successfully logged in.Welcome :{entered_user_name} to your account")
    else :
        print("Invalid user_name or user_password")
        print("User_name")
        entered_user_name=input()
        print("user_Password")
        entered_user_password=input()


    print('\n')


    while True:
            print("Use these short codes : cd - create a new details, dd - display details,del - delete details fd -find details, ex -exit the details list ")

            short_code = input().lower()

            if short_code == 'cd':
                    print("New Details")
                    print("-"*30)

                    print ("Account_socialmedia ....")
                    account_socialmedia = input()

                    print("User_name ...")
                    user_name = input()

                    while True:
  
                      print("Use the following shortcodes : cp-create password or gp-to get a system generated password")
                      user_password_type = input().lower()
                      if user_password_type == 'cp':
                          user_password = input("Create your password\n")
                          break
                      elif user_password_type== "gp":
                          print('Hello, Welcome to User_Password Locker!')
                          length = int(input('\nEnter the length of user_password: '))
                          user_password= generate_password(length)
                          print("\n")
                          print(f"Your generated user_password is : {user_password}")
                          break

                      
                      else:
                          print("Invalid shortcode please try again")
                    
                   
                    save_details(create_details(account_socialmedia, user_name, user_password))                    
                    print ('\n')
                    print(f"New Details Account socialmedia:{account_socialmedia}, User_name:{user_name},user_Password: {user_password}")
                    print ('\n')

            elif short_code == 'dd':

                    if display_details():
                            print("Here is a list of all your details")
                            print('\n')

                            for details in display_details():
                                    print("Account_socialmedia: "+ str(details.account_socialmedia) + "  User_name: "+str(details.user_name)+ "  user_password: " +str(details.user_password))

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any details saved yet")
                            print('\n')

            elif short_code == 'fd':

                    print("Enter the account_socialmedia you want to search for")

                    search_account_socialmedia = input()
                    if check_existing_details(search_account_socialmedia):
                            search_details = find_details(search_account_socialmedia)
                            search_details.find_by_account_socialmedia(search_account_socialmedia)
                            print('\n')
                            print(f"Account_socialmedia.......{search_details.account_socialmedia}")
                    else:
                            print("The details doesn't exist")

            elif short_code == "del":


                print("Enter account name of the Details you want to delete")

                search_account_socialmedia = input()
                if find_details(search_account_socialmedia):
                        search_details = find_details(search_account_socialmedia)
                        print("_"*40)
                        search_details.delete_details()
                        print('\n')
                        print(f"Your details for : {search_details.account_socialmedia} successfully deleted!!!")
                        print('\n')
                else:
                        print("The Delete you want to delete does not exist")

            elif short_code == "ex":
                    print("Enjoy your time .......")
                    break
            else:
                    print("Please use the short codes, If the issue is unresolved Reach out to us for help")

if __name__ == '__main__':
    main()
