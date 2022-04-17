import numpy as np


class Vehicle:

    def __init__(self, x, y, length=1):
        """
        Initiates the Vehicle class

        Parameters
        ----------
        length : length of the vehicle
        """

        self.length = length    # Length of the vehicle, default is 1 slot in the array
        self.react_time = 1.5   # In seconds
        self.speed = 80.        # Default speed
        self.ref_speed = 130.   # Desired speed (130 km/h on highways)
        self.smoothness = 4.    # See https://towardsdatascience.com/simulating-traffic-flow-in-python-ee1eab4dd20f
        # for delta explanation and https://traffic-simulation.de/info/info_IDM.html for value
        self.ref_accel = 0.3    # In m²/s
        self.ref_decel = 3.0    # In m²/s
        self.min_gap = 4.       # In meter
        self.x = x              # Vertical position from 0 to width - 1
        self.y = y              # Horizontal position from 0 to length - 1
        self.type = 1           # Type of vehicle

    def update_speed(self):
        pass

    def calculate_accel(self, leader):
        s0 = self.min_gap
        s = self.get_gap(self, leader)
        v = self.speed
        delta_v = self.speed - leader.speed
        T = self.react_time
        a = self.ref_accel
        b = self.ref_decel
        delta = self.smoothness
        v0 = self.ref_speed

        s_star = s0 + max(0., v * T + (v * delta_v/(2*np.sqrt(a * b))))
        new_accel = a * (1 - (v/v0)**delta - (s_star/s) ** 2)

        return new_accel

    def get_gap(self, road, veh2):
        """
        :param road: Road object
        :param veh2: Other vehicle
        :return: gap - The value of the gap between the vehicle 1 and the vehicle 2

        Calculates the gap between two vehicles assuming the given vehicle is ahead and return the absolute value of it
        """
        # Only 1D for now

        gap = veh2.y - self.y - 1   # Gap is bumper to bumper so [self, 0, 0, veh2] is a gap of 2 cell
        if gap < 0:
            gap += road.length  # Case in which the leader is at the opposite side of the array but still
            # ahead (infinite road)

        return gap

    def change_lane(self, dest_lane):
        """
        Changes the lane of the vehicle to the destination lane

        Parameters
        ----------
        dest_lane

        Returns
        -------

        """
        pass


class Car(Vehicle):

    def __init__(self, length):
        super().__init__(length)


class Truck(Vehicle):

    def __init__(self, length):
        super().__init__(length)
