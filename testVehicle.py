import unittest
from vehicle import Vehicle

class TestRoad(unittest.TestCase):
    def testInit(self):
        v=Vehicle(3,2,1)
        self.assertEqual(v.x,3)
        self.assertEqual(v.y,2)
        self.assertEqual(v.length,1)




if __name__=='__main__':
    unittest.main()