
class Vehicle:

    def __init__(self, weight, react_time,length=1):
        """
        Initiates the Vehicle class

        Parameters
        ----------
        length : length of the vehicle
        weight : weight of the vehicle
        react_time :  reaction time of the driver
        """

        self.length = length
        self.weight = weight
        self.react_time = react_time

    def forward(self):
        """
        Makes the vehicle go forward depending on its speed
        Returns
        -------
        Nothing
        """

        pass

    def brake(self, amount):
        """
        Reduces the speed of the vehicle depending on the amount

        Parameters
        ----------
        amount

        Returns
        -------

        """
        pass

    def throttle(self, amount):
        """
        Increases the speed of the vehicle depending on the amount

        Parameters
        ----------
        amount

        Returns
        -------

        """
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

    def __init__(self, length, weight, react_time):
        super().__init__(length, weight, react_time)


class Truck(Vehicle):

    def __init__(self, length, weight, react_time):
        super().__init__(length, weight, react_time)