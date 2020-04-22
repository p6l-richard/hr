from solution import parse_input
import unittest

input1 = """6
1 2 3 4 10 11""" 
input2 = """0""" 
input3 = """0
"""
input4 = """6
1 2 3 4 10 11
""" 
input5 = """
"""
input6 = """
6
1 2 3 4 10 11"""
input7 = """0

1 2 3 4 10 11"""

input8 = """
6

1 2 3 4 10 11

"""

input9 = """2.4
1 2 3 4 10 11
"""

input10 = """
0

1 2 3 4 10 11

"""

input_list = [input1, input2, input3, input4, input5, input6, input7, input8]

result = [6, list(map(lambda el: float(el),[1,2,3,4,10,11]))]
class TestParse(unittest.TestCase):
    print('I got imported')
    def test_parse_input(self):
        self.assertEqual(result, parse_input(input1))
        self.assertEqual('Input does not contain 2 lines', parse_input(input2))
        self.assertEqual('Input does not contain 2 lines', parse_input(input3))
        self.assertEqual(result, parse_input(input4))
        self.assertEqual('Input does not contain 2 lines', parse_input(input5))
        self.assertEqual(result, parse_input(input6))
        self.assertEqual('length and array-length do not match', parse_input(input7))
        self.assertEqual(result, parse_input(input8))
        self.assertEqual('First value is no integer', parse_input(input9))
        self.assertEqual('length and array-length do not match', parse_input(input10))


if __name__ == '__main__':
    unittest.main()
