import unittest

def alphabet2number(alphabet):
    if alphabet == "a":
        return 1
    elif alphabet == "b":
        return 2
    elif alphabet == "c":
        return 3
    elif alphabet == "d":
        return 4
    elif alphabet == "e":
        return 5
    elif alphabet == "f":
        return 6
    elif alphabet == "g":
        return 7
    elif alphabet == "h":
        return 8
    elif alphabet == "i":
        return 9



class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected = 9
        actual = alphabet2number("i")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()