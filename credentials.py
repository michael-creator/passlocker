class Credential:
    """
    class that generate new instances of credentials
    """
    credentials_list = []
    def __init__(self, username, account_name, account_password):
        self.username = username
        self.account_name = account_name
        self.account_password = account_password
    def save_credential(self):
        """
        save_credential method  saves credential into credential_list
        """
        Credential.credentials_list.append(self)
    def delete_credentials(self):
        """
        delete_credential method to delete a saved credential from credential_list
        """
        Credential.credentials_list.remove(self)
    @classmethod
    def find_by_name(cls, account_name):
        """
        method that takes in a account name and returns  credential that matches that account name
        
        """
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential
    @classmethod
    def credential_exists(cls, acc_name):
        '''
        checks if  credential object exists from the credential  list.
       
        '''
        for credential in cls.credentials_list:
            if credential.account_name == acc_name:
                return True
        return False

