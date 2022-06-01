import unittest
from road import Road
from vehicle import Vehicle, Car, Truck


class Test_road(unittest.TestCase):

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


class Test_vehicles(unittest.TestCase):

    road = Road(100, 3, 10)

    def test_Init_Car(self):
        """
        Checks that the value given to the constructor are correctly set as instance variables.

        :return: Nothing
        :raise Exception: If the values given to the constructor are not set properly as instance variables or do not have matching values
        :author: Mipam Quici
        """
        v = Car(3, 2, self.road, 1)
        self.assertEqual(v.x, 3)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.length, 1)

        with self.assertRaises(ValueError):
            v2 = Car(10, 2, self.road, 1)

    def test_Init_Truck(self):

        v = Truck(1, 6, self.road)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 6)
        self.assertEqual(v.length, 3)

        with self.assertRaises(ValueError):
            v2 = Truck(1, 100, self.road, 3)

    def test_Id_Not_Equals(self):

        v1 = Car(1, 8, self.road, 1)
        v2 = Truck(2, 5, self.road)
        self.assertNotEqual(v1.id, v2.id)



if __name__ == '__main__':
    unittest.main()
