import unittest
import dataMax as proj

class MyTestCase(unittest.TestCase):
    def test_count(self):
        self.assertEqual([proj.top3.index[0], proj.top3.index[1], proj.top3.index[2]], [' Australia ', ' USA ', ' New Zealand '])

    def test_count(self):
        self.assertTrue([proj.top3.index[0], proj.top3.index[1], proj.top3.index[2]], [' Australia ', ' USA ', ' New Zealand '])



if __name__ =='__main__':
    unittest.main()