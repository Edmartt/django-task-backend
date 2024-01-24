import re

class PasswordChecker:
    
    def __init__(self) -> None:
        pass
    
    def compare_password(self, password, compared_password) -> bool:
        '''
        checks if two strings are equals in password input
        '''
          
        return True if password ==compared_password else False
    
    def check_password_length(self, password) -> bool:
        '''
        checks password length. Minimun accepted is 8 characters
        '''
        return True if len(password) >= 8 else False
    
    def check_password_chars(self, password) -> bool:
        '''
        checks if a pattern based on uppercase, lowercase and numbers is matched
        '''
        pattern = r'^(?=.*[a-z])(?=.*[A-Z](?=.*\d)).+$'
        
        return True if re.match(pattern, password) else False
            