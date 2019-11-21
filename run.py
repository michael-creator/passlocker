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
    
