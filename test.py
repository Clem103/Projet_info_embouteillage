import unittest
from road import Road
from vehicle import Vehicle


class Test(unittest.TestCase):

    def test_Init_Road(self):
        """
        Checks that the value given to the constructor are correctly set as instance variables.

        :return: Nothing
        :raise Exception: If the values given to the constructor are not set properly as instance variables or do not have matching values
        :author: Mipam Quici
        """
        r = Road(10, 1, 3)
        self.assertEqual(r.length, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.nbvehic, 3)

    def test_Init_Except_Road(self):
        """
        Checks that Exception are correctly handled when creating a Road with valid and invalid parameters.

        :return: Nothing
        :raise Exception: If the Exception caused by invalid or valid values are not correctly raised
        :author: Mipam Quici
        """
        with self.assertRaises(Exception):
            r = Road(-23, 50, 2)
        with self.assertRaises(Exception):
            r = Road(23, 0, 2)
        with self.assertRaises(Exception):
            r = Road(10, 10, 103)

    def test_Init_Vehicle(self):
        """
        Checks that the value given to the constructor are correctly set as instance variables.

        :return: Nothing
        :raise Exception: If the values given to the constructor are not set properly as instance variables or do not have matching values
        :author: Mipam Quici
        """
        r = Road(10, 1, 3)
        v = Vehicle(3, 2, r, 1)
        self.assertEqual(v.x, 3)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.length, 1)


if __name__ == '__main__':
    unittest.main()
