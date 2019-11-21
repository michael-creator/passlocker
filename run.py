import random
from user import User
from  credentials import Credential
def create_user(username, password):
    """
    function that create enable a person to create a new user
    """
    new_user = User()
    return new_user
def create_credential(username, account_name, account_password):
    """
    function to enable a person to create a new credential
    """
    new_credential = Credential (username, account_name, account_password)
    return new_credential
def save_user(user):
    """
    function that save new created user
    """
    user.save_user()
def save_credential(Credential):
    """
    function that save credential
    """
    Credential.save_credential()
    
def check_existing_user(name):
    '''
    check if user exists
    '''
    return User.user_exists(name)

def find_credential(account_name):
    '''
    Function that finds credentials by account name
    '''
    # new_credential = Credential(acc, name, password)
    return Credential.find_by_name(account_name)

def existing_credentials(name):
    '''
    Functiion that checks if an account really exists
    '''
    Credential.credential_exists(name)
    
def user_exist (name):
    """
    Functiion that checks if an account really exists
    """
    User.user_exists(name)
    return name
def delete_credential(credentials):
    '''
    Function that deletes credentials that are no longer in use
    '''
    return Credential.delete_credentials(credentials)
def display_credential():
    '''
    Functiomn that displays all the saved credentials
    '''
    return Credential.display_credentials()

def main():
    while True:
        print(" PASS LOCKER ")
        print('_'*30)
        print("Do you wish to create account with pass locker? yes/no")
        print("use Short code 'ex' to  exit")
        option = input().lower()
        if option == "yes":
            print('* Login ')
            print('Input username \n')
            nomname = input()
            print('\n')
            print('Input password')
            nompass = input()
            authentication = user_exist(nomname)
            if authentication == True:
                print(f"Welcome:{nomname} to your Account ")
                print('*'*40)
                print("Select an option either a,b,c,d or e")
                print('\n')
                while True:
                    print('1:Add credential')
                    print('2:View saved credential')
                    print('3:Delete Credentials')
                    print('4:Search Credentials')
                    print('5:Leave')
                    