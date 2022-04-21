import numpy as np


class Vehicle:

    def __init__(self, x, y, road, length=1):
        """
        :param x: Vertical position of the vehicle
        :param y: Horizontal position of the vehicle
        :param road: Road object where the vehicle is located
        :param length: Length of the vehicle

        Initiates the Vehicle class
        """

        self.road = road
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

    def update_speed(self, leader, dt):
        dv = self.calculate_accel(leader)
        new_speed = self.speed + dv * dt
        if new_speed <= 0:
            new_speed = 0
        new_y = int(np.round(self.y + self.speed * dt + 1/2 * dv * dt**2)) % self.road.length
        self.speed = new_speed
        self.y = new_y

    def calculate_accel(self, leader):
        s0 = self.min_gap
        s = self.get_gap(leader)
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

    def get_gap(self, leader):
        """
        :param leader: Other vehicle
        :return: gap - The value of the gap between the vehicle 1 and the vehicle 2

        Calculates the gap between two vehicles assuming the given vehicle is ahead and return the absolute value of it
        """
        # Only 1D for now

        gap = leader.y - self.y - 1   # Gap is bumper to bumper so [self, 0, 0, veh2] is a gap of 2 cells
        if gap < 0:
            gap += self.road.length  # Case in which the leader is at the opposite side of the array but still
            # ahead (infinite road)

        if gap == 0:
            gap = 0.0001

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

    def __init__(self, x, y, length):
        super().__init__(x, y, length)


class Truck(Vehicle):

    def __init__(self, x, y, length):
        super().__init__(x, y, length)
