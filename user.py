class User:
    """
    Class that generate new instance of us user.
    """
    user_list = []
    def ___init___(self, login_username, user_password):
        '''
        initiating the variables
        '''
        self.login_username = login_username
        self.user_password = user_password
    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)
    