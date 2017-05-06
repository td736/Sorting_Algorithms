from SelectionSort import SelectionSort
import unittest


class SelectionSortTest(unittest.TestCase):



    def test_init(self):
        sortTest = SelectionSort(['a'])
        
        self.assertEqual(sortTest.unsorted,['a'])
        self.assertEqual(sortTest.sorted, [])


    def test_sortNext(self):
        sortTest = SelectionSort(['a', 1.2, 4])
        sortTest.sortNextElement()
        sortTest.sortNextElement()

        self.assertEqual(sortTest.unsorted,['a'])
        self.assertEqual(sortTest.sorted,[1.2, 4])


    def test_sortFully(self):
        sortTest = SelectionSort(['abc', 1.0, 'ab', 'aa', 3, 1.2, 4, 'abb'])
        sortTest.sortFully()

        self.assertEqual(sortTest.unsorted,[])
        self.assertEqual(sortTest.sorted,[1.0, 1.2, 3, 4, 'aa', 'ab', 'abb', 'abc'])
        


                             
if __name__ == '__main__':
    unittest.main()
