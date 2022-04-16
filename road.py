import numpy as np
from random import randint
from vehicle import Vehicle


class Road(np.ndarray):
    def __new__(cls, length: int, width: int, vehicles: list):
        """
        :param length: Length of the road (equal to the maximum number of vehicle that can fit)
        :param width: Number of lane
        :param vehicles: Array (list) of Vehicle that need to be placed into the road

        Creates the Road object and overrides the ndarray constructor to add instance variables specific to our project
        """

        obj = super(Road, cls).__new__(cls, (width, length), dtype=Vehicle)
        obj.fill(0)

        obj.nbvehic = len(vehicles)
        obj.length = length
        obj.width = width
        obj.vehicles = vehicles

        return obj

    def __array_finalize__(self, obj):
        """
        :param obj: Object being manipulated
        :return: Nothing

        Called when a new array is created (e.g. when ndarry.__new__ is called).
        When it is called via an explicit constructor obj is None.
        When it is called via a method which involves the creation of a new array, the __new__ method defined above
        isn't necessarily called. Therefore, this methods purpose is to make sure the instance variables are passed
        over the object transformation
        """
        if obj is None:
            return

        self.nbvehic = getattr(obj, 'nbvehic', None)
        self.length = getattr(obj, 'length', None)  # NB: These variables don't reflect the correct shape of the array
        self.width = getattr(obj, 'width', None)    # when doing splicing (because they don't get updated anywhere)
        self.vehicles = getattr(obj, 'vehicles', None)

    # noinspection PyMissingConstructor
    def __init__(self, length: int, width: int, vehicles: list) -> None:
        """
        :param length: Length of the road (equal to the maximum number of vehicle that can fit)
        :param width: Number of lane
        :param vehicles: Array (list) of Vehicle that need to be placed into the road
        :raise ValueError: If the number of vehicles exceeds the available space or if the width or the length of the
            road is inferior or equal to 0

        Initiates a road that is *length* long and with *width* lane by placing the given vehicles on the road.
        """

        if self.width <= 0 or self.length <= 0:
            raise ValueError("Road dimensions are not correct")

        if self.nbvehic >= self.length*self.width:
            raise (ValueError("Too many vehicles"))

        self.place_vehicles()

    def __str__(self):
        r = ""
        for x in range(self.width):
            for y in range(self.length):
                if self[x, y] == 1:
                    r += "C"
                elif self[x, y] == 2:
                    r += "T"
                else:
                    r += "_"
            r += "\n"

        return r

    def place_vehicles(self):
        for veh in self.vehicles:
            x = randint(0, self.width-1)
            y = randint(0, self.length-1)
            while self[x, y] != 0:
                x = randint(0, self.width - 1)
                y = randint(0, self.length - 1)
            self[x, y] = veh
            print("Placing vehicle of type {0} at coord {1}".format(veh, (x,y)))
            print(self)

    # soucis avec les randint: il peut sortir une paire de coordonnées égales, on aura dans ce cas 1 voiture en moins.

        # for j in range(self.width):
        #     for k in range(self.length-2):
        #         #permet de vérifier l'espacement entre deux véhicule au début de la simulation
        #         if coordinit[j][k+1]==0 and coordinit[j][k]==0:
        #             coordinit[j][k+1]=1
        #             coordinit[j][k+2]=0
        #         if coordinit[j][k+1]==2 and coordinit[j][k]==2:
        #             coordinit[j][k+1]=1
        #             coordinit[j][k+2]=2
        #         if coordinit[j][k+1]==0 and coordinit[j][k]==2:
        #             coordinit[j][k+1]=1
        #             coordinit[j][k+2]=0
        #         if coordinit[j][k+1]==2 and coordinit[j][k]==0:
        #             coordinit[j][k+1]=1
        #             coordinit[j][k+2]=2


    def turn(self):
        """
        creates a turn in which our vehicles will move
        :return:
        """
        pass


    def simlulate(self):
        """
        simulation of a turn
        :return:
        """
        pass


if __name__ == "__main__":
    veh_arr = [Vehicle(1) for i in range(0,7)]
    a = Road(10, 1, veh_arr)
