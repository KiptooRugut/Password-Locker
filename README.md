# Password-Locker

## By [Kiptoo Mike](https://github.com/KiptooRugut) ,February 2022

## Description

Application that will help us manage usernames, passwords and even generate new passwords for us.

## Setup/Installation Instructions

### To get the project into your local machine

* Open your terminal
* Create a folder and navigate to the folder you created.
* Run `git clone https://github.com/KiptooRugut/Password-Locker.git`
* Run `cd Password-Locker` command to confirm it was successfully cloned.

### To run this application

* Open the cloned project in your editor e.g `code .` to open in visual studio code editor.
* On the terminal run these commands:
* `chmod +x run.py`
* `./run.py`

## User Stories

As a user, i want to :

* Create a password locker account with my details, a login username and password.
* Store my already existing account details in the application.
* Create new account details in the application and the application generates a password for me.
* The user has the option of putting in a password that he/she want to use for the new details account.
* View my various account details and their passwords in the application.
* Delete details account that the user no longer needs in the application.

## Behavior Driven Development

|               Behaviour              | Input                            | Output                                               |
|:------------------------------------:|----------------------------------|------------------------------------------------------|
| Open the application on the terminal | Run the command **./run.py** | Hello Welcome to your password locker!Proceed to create your account |
| Create a username and password        | Enter a username of your choice and password     | Hello **username**,Account created succesfully! Your password is:**password**|
| Proceed to login |   Enter your **username** and **password** | Welcome: **username** to your account |
| Create new detail | Enter **cc** | Enter account name and username then enter **cp** to create your own password or **gp** to get a system generated password where you'll have to specify length of the password you need | New detail **Account name**, **Username**,**Password** |
| Display stored details       |           Enter ***dc***         | A list of all details that has been stored or It shows that you don't have any details saved yet|
| Delete an existing detail that you no longer need| Enter **del** |Enter the account name of the Detail you want to delete and returns true if the it has been deleted and false if it doesn't exist|
|  Exit the application                |              Enter **ex**       | Exits the application |

## Technologies used

* Python3.8

## Support and contact details

Reach out to me through the following email addresses:

* mike.kiptoo@student.moringaschool.com.
* mccrug97@gmail.com.

### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE).
