#################
#    Imports    #
#################

import unittest
from palindrome import check_palindrome

#################
#   Testing     #
#################

class Test_W_Count(unittest.TestCase):
    
    def test_empty_string(self):
        input_sample = ''
        output = True
        self.assertEqual(check_palindrome(input_sample), output)

    def test_easy_string_1(self):
        input_sample = 'holaaloh'
        output = True
        self.assertEqual(check_palindrome(input_sample), output)

    def test_easy_string_2(self):
        input_sample = 'neuquen'
        output = True
        self.assertEqual(check_palindrome(input_sample), output)

    def test_false_string(self):
        input_sample = 'holanda'
        output = False
        self.assertEqual(check_palindrome(input_sample), output)

    def test_space_string(self):
        input_sample = 'hola a l o h'
        output = True
        self.assertEqual(check_palindrome(input_sample), output)

if __name__ == '__main__':
    unittest.main()
