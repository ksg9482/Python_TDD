import unittest
import calculations

class TddTest(unittest.TestCase):

    def test_add(self):
        result = calculations.add(5, 10)
        if result == 15:
            print('Add test OK')
        else:
            print('Add test Error')

if __name__ == '__main__':
    unittest.main()