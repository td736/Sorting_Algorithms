from InsertionSort import InsertionSort
import unittest


class InsertionSortTest(unittest.TestCase):



    def test_init(self):
        sortTest = InsertionSort(['a'])
        
        self.assertEqual(sortTest.unsorted,['a'])
        self.assertEqual(sortTest.sorted, [])


    def test_sortFirst(self):
        sortTest = InsertionSort([2, 1])
        sortTest.sortFirstElement()
        
        self.assertEqual(sortTest.unsorted,[1])
        self.assertEqual(sortTest.sorted,[2])


    def test_sortNext(self):
        sortTest = InsertionSort(['a', 1.2, 4])
        sortTest.sortNextElement()
        sortTest.sortNextElement()

        self.assertEqual(sortTest.unsorted,[4])
        self.assertEqual(sortTest.sorted,[1.2, 'a'])


    def test_sortFully(self):
        sortTest = InsertionSort(['abc', 1.0, 'ab', 'aa', 3, 1.2, 4, 'abb'])
        sortTest.sortFully()

        self.assertEqual(sortTest.unsorted,[])
        self.assertEqual(sortTest.sorted,[1.0, 1.2, 3, 4, 'aa', 'ab', 'abb', 'abc'])
        

                             
if __name__ == '__main__':
    unittest.main()
