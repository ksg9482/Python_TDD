import unittest
from number_to_roman import number_to_roman

class number_to_roman_test(unittest.TestCase):
   
    def test_convert_1(self):
        result = number_to_roman.convert(self, 1)
        if result == 'I':
            print('clear')
        else:
            print('1을 로마자로 바꾸면 I여야 합니다.')

    def test_convert_array(self):
        number_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = number_to_roman.convert(self, number_arr)
        if result == ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']:
            print('clear')
        else:
            print('각 숫자를 로마자로 바꾼 배열이 반환되어야 합니다.')

    def test_convert_1_string(self):
        result = number_to_roman.convert(self, '1')
        if result == 'I':
            print('clear')
        else:
            print('1이 문자열이라도 로마자로 바꾸면 I여야 합니다.')
    
    def test_convert_0(self):
        result = number_to_roman.convert(self, 0)
        if result == '로마자 0은 존재하지 않습니다.':
            print('clear')
        else:
            print('로마자 0은 존재하지 않습니다.')

    

if __name__ == '__main__':
    unittest.main()