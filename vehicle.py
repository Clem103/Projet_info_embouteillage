class Vehicle:

    def __init__(self, length=1):
        """
        Initiates the Vehicle class

        Parameters
        ----------
        length : length of the vehicle
        """

        self.length = length
        # self.weight =
        # self.react_time =
        # self.speed =
        # self.max_speed=
        # self.smoothness=

    def update_speed(self):
        pass

    def change_lane(self, dest_lane):
        """
        Changes the lane of the vehicle to the destination lane

        Parameters
        ----------
        dest_lane

        Returns
        -------

        """


class Car(Vehicle):

    def __init__(self, length):
        super().__init__(length)


class Truck(Vehicle):

    def __init__(self, length):
        super().__init__(length)
