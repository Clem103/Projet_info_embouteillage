from __future__ import annotations
import numpy as np


class Vehicle:

    def __init__(self, x: int, y: int, road: 'Road', length: int = 1) -> None:
        """
        Initiates the Vehicle class on the given road at given coordinates.

        :param x: Vertical position of the vehicle
        :param y: Horizontal position of the vehicle
        :param road: Road object where the vehicle is located
        :param length: Length of the vehicle
        :author: Clément Vellu
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

    def update_speed(self, leader: Vehicle, dt: float) -> None:
        """
        Updates the speed of the vehicle using the ballistic method.

        :param leader: Vehicle that is ahead.
        :param dt: Time increment used in simulation
        :return: Nothing
        :author: Clément Vellu
        """
        dv = self.calculate_accel(leader)
        new_speed = self.speed + dv * dt
        if new_speed <= 0:
            new_speed = 0
        new_y = int(np.round(self.y + self.speed * dt + 1/2 * dv * dt**2)) % self.road.length
        self.speed = new_speed
        self.y = new_y

    def calculate_accel(self, leader: Vehicle) -> float:
        """
        Calculates the acceleration of the vehicle using the Intelligent Driver Model (IDM).
        Called by Vehicle.update_speed.

        :param leader: Vehicle that is ahead
        :return: new_accel: Calculated acceleration
        :author: Clément Vellu
        """
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
        Calculates the gap between two vehicles assuming the given vehicle is ahead and return the absolute value of it.

        :param leader: Other vehicle
        :return: gap - The value of the gap between the vehicle 1 and the vehicle 2
        :author: Mipam Quici
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
        NOT YET IMPLEMENTED - Changes the lane of the vehicle to the dest_lane.

        :param dest_lane: Lane that the driver wants to reach
        :return: Nothing
        :author: None yet
        """
        pass


### NOT YET IMPLEMENTED - Classes that inherits from Vehicle with different parameters for the model ###

class Car(Vehicle):

    def __init__(self, x, y, road, length):
        super().__init__(x, y, road, length)


class Truck(Vehicle):

    def __init__(self, x, y, road, length):
        super().__init__(x, y, road, length)
