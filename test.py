import unittest
from road import Road

class TestRoad(unittest.TestCase):
    def testInit(self):
        r=Road(10,1,3)
        self.assertEqual(r.length,10)
        self.assertEqual(r.width,1)
        self.assertEqual(r.nbvehic,3)







if __name__=='__main__':
    unittest.main()