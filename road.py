import numpy as np
from random import randint
from vehicle import Vehicle


class Road(np.ndarray):
    def __new__(cls, length: int, width: int, nb_vehicle: int):
        """
        :param length: Length of the road (equal to the maximum number of vehicle that can fit)
        :param width: Number of lane
        :param nb_vehicle: Number of Vehicle that need to be placed into the road

        Creates the Road object and overrides the ndarray constructor to add instance variables specific to our project
        """

        obj = super(Road, cls).__new__(cls, (width, length), dtype=Vehicle)
        obj.fill(0)

        obj.nbvehic = nb_vehicle
        obj.length = length
        obj.width = width
        obj.vehicles = []

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
    def __init__(self, length: int, width: int, nb_vehicle: int) -> None:
        """
        :param length: Length of the road (equal to the maximum number of vehicle that can fit)
        :param width: Number of lane
        :param nb_vehicle: Number of Vehicle that need to be placed into the road
        :raise ValueError: If the number of vehicles exceeds the available space or if the width or the length of the
            road is inferior or equal to 0

        Initiates a road that is *length* long and with *width* lane by placing the given vehicles on the road.
        """

        if self.width <= 0 or self.length <= 0:
            raise ValueError("Road dimensions are not correct")

        if self.nbvehic >= self.length*self.width:
            raise (ValueError("Too many vehicles"))

        self.place_vehicles_1d()

    def __str__(self):
        r = ""
        for x in range(self.width):
            for y in range(self.length):
                if self[x, y] != 0:
                    if self[x, y].type == 1:
                        r += "C"
                    elif self[x, y].type == 2:
                        r += "T"
                else:
                    r += "_"
            r += "\n"

        return r

    def place_vehicles_1d(self):
        target_gap = self.length // self.nbvehic - 1

        y = 0
        for i in range(self.nbvehic):
            self[0, y] = Vehicle(0, y)
            self.vehicles.append(self[0, y])
            y += target_gap + 1
        print(self)

    def place_vehicles_randomly(self):
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


if __name__ == "__main__":
    a = Road(1000, 1, 50)  # Kept at 1 lane for the moment and 1000 cell long (scale for 4km simulation)
