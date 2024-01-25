from django.test import TestCase
from api.users.utils.password_checks import PasswordChecker

class UserTests(TestCase):
    
    def setUp(self):
        self.pass_checker = PasswordChecker()
    
    def tearDown(self):
        del self.pass_checker
    
    def test_password_equals(self):
        result = self.pass_checker.compare_password('1234567','1234567')
        self.assertTrue(result)
    
    def test_password_not_equals(self):
        result = self.pass_checker.compare_password('1234567', '12345678')
        self.assertFalse(result)
        
    def test_password_length_longer_than_8(self):
        result = self.pass_checker.check_password_length('123456789')
        self.assertTrue(result)
    
    def test_password_length_smaller_than_8(self):
        result = self.pass_checker.check_password_length('1234567')
        self.assertFalse(result)
    
    def test_password_chars_pattern_true(self):
        '''test string pattern containing lowercase, uppercase and numbers in any order'''
        result = self.pass_checker.check_password_chars('aBkakjk123')
        result2 = self.pass_checker.check_password_chars('BhhgVh12')
        self.assertTrue(result)
        self.assertTrue(result2)
    
    def test_password_chars_pattern_false(self):
        result1 = self.pass_checker.check_password_chars('abcde')
        result2 = self.pass_checker.check_password_chars('SAJHJHSAJ')
        result3 = self.pass_checker.check_password_chars('asadasKHKJHKJH')
        result4 = self.pass_checker.check_password_chars('asdads21324aas')
        result5 = self.pass_checker.check_password_chars('767ASJASJH')
        
        self.assertFalse(result1)
        self.assertFalse(result2)
        self.assertFalse(result3)
        self.assertFalse(result4)
        self.assertFalse(result5)
    
    def test_password_strength(self):
        strong_password_string = 'HasasdahUI789'
        
        strong_length_result = self.pass_checker.check_password_length(strong_password_string)
        strong_equals_result = self.pass_checker.compare_password(strong_password_string, 'HasasdahUI789')
        strong_pattern_result = self.pass_checker.check_password_chars(strong_password_string)
        
        assert strong_length_result and strong_equals_result and strong_pattern_result
        
    def test_password_weakness(self):
        '''check if at least one condition is false to know the weakness of the password'''
        weak_password_string = 'abjjhasjd'
        
        weak_length_result = self.pass_checker.check_password_length(weak_password_string)
        weak_equals_result = self.pass_checker.compare_password(weak_password_string, 'abjjhasjd')
        weak_pattern_result = self.pass_checker.check_password_chars(weak_password_string)
        
        assert not all([weak_length_result, weak_equals_result, weak_pattern_result])
        
        