import numpy as np
from random import randint
from vehicle import Vehicle, Car, Truck


class Road(np.ndarray):

    def __new__(cls, length: int, width: int, nb_vehicle: int):
        """
        Creates the Road object and overrides the ndarray constructor to add instance variables specific to our project.

        :param length: Length of the road (equal to the maximum number of vehicle that can fit)
        :param width: Number of lane
        :param nb_vehicle: Number of Vehicle that need to be placed into the road
        :author: Clément Vellu
        """

        obj = super(Road, cls).__new__(cls, (width, length), dtype=Vehicle)
        obj.fill(0)

        obj.nbvehic = nb_vehicle
        obj.length = length
        obj.width = width
        obj.vehicles = []

        return obj

    def __array_finalize__(self, obj: np.ndarray) -> None:
        """
        Called when a new array is created (e.g. when ndarray.__new__ is called). \n
        When it is called via an explicit constructor obj is None.

        When it is called via a method which involves the creation of a new array, the __new__ method defined above
        isn't necessarily called. Therefore, this method's purpose is to make sure the instance variables are passed
        over the object transformation.

        :param obj: Object being manipulated
        :return: Nothing
        :author: Clément Vellu
        """
        if obj is None:
            return

        self.nbvehic = getattr(obj, 'nbvehic', None)
        self.length = getattr(obj, 'length', None)  # NB: These variables don't reflect the correct shape of the array
        self.width = getattr(obj, 'width', None)    # when doing splicing (because they don't get updated anywhere)
        self.vehicles = getattr(obj, 'vehicles', None)

    # noinspection PyMissingConstructor
    def __init__(self, length: int, width: int, nb_vehicle: int) -> None:
        """
        Initiates a road that is *length* long and with *width* lane by placing the given vehicles on the road.

        :param length: Length of the road (equal to the maximum number of vehicle that can fit)
        :param width: Number of lane
        :param nb_vehicle: Number of Vehicle that need to be placed into the road
        :raise ValueError: If the number of vehicles exceeds the available space or if the width or the length of the
            road is inferior or equal to 0
        :author: Mipam Quici
        """

        if self.width <= 0 or self.length <= 0:
            raise ValueError("Road dimensions are not correct")

        if self.nbvehic >= self.length*self.width:
            raise (ValueError("Too many vehicles"))

        self.place_vehicles_1d()

    def __str__(self) -> str:
        """
        Displays the road.

        :return r: String that will be displayed when called
        :author: Mipam Quici
        """
        r = ""
        for x in range(self.width):
            for y in range(self.length):
                if self[x, y] != 0:
                    r += str(self[x, y])
                else:
                    r += "_"
            r += "\n"

        return r

    def place_vehicles_1d(self):
        """
        Called upon initialization of the simulation to instantiate the vehicles and to place them as spread as possible
        using the simulation parameters (length of the road and number of vehicles).

        :return: Nothing
        :author: Clément Vellu
        """
        target_gap = self.length // self.nbvehic - 1
        y = 0
        for i in range(self.nbvehic):
            if randint(1, 11) >= 3:
                self[0, y] = Car(0, y, self, 1)
            else:
                self[0, y] = Truck(0, y, self, randint(2, 5))
            self.vehicles.append(self[0, y])
            print("Placing vehicle at coord {0}".format((0, y)))
            y += target_gap + 1

        print(self)



    def place_vehicles_randomly(self):
        """
        Shuffles the location of vehicles.

        :return: Nothing
        :author: Mipam Quici
        """
        self.fill(0)
        print("Shuffling vehicles location")
        for veh in self.vehicles:
            x = randint(0, self.width - 1)
            y = randint(0, self.length - 1)
            while self[x, y] != 0:
                x = randint(0, self.width - 1)
                y = randint(0, self.length - 1)
            self[x, y] = veh
            veh.x = x
            veh.y = y

            print(self)

    def update_pos(self):
        """
        Updates the position of the vehicles on the road and brings the vehicles that reach the end of the road to
        the beginning of it. \n
        Usually called for each step of the simulation.

        :return: Nothing
        :author: Clément Vellu
        """
        self.fill(0)

        for veh in self.vehicles:
            y = veh.y % self.length
            self[0, y] = veh


if __name__ == "__main__":
    # For testing purpose
    a = Road(100, 1, 2)  # Kept at 1 lane for the moment and 1000 cell long (scale for 4km simulation)