from Main import Main
import unittest


class MainTest(unittest.TestCase):



    def test_inputValidation(self):
        self.assertRaises(AssertionError, Main, 'a')
        self.assertRaises(AssertionError, Main, [1,2,3,[]])
        self.assertRaises(AssertionError, Main, [1,2,3,True])



if __name__ == '__main__':
    unittest.main()
