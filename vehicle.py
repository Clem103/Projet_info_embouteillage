from __future__ import annotations
import numpy as np
from abc import ABC, abstractmethod
from random import randint
from PyQt5 import QtGui, QtCore


class Vehicle(ABC):
    id = 0

    def __init__(self, x: int, y: int, road: 'Road', length: int) -> None:
        """
        Initiates the Vehicle class on the given road at given coordinates.

        :param x: Vertical position of the vehicle
        :param y: Horizontal position of the vehicle
        :param road: Road object where the vehicle is located
        :param length: Length of the vehicle
        :author: Clément Vellu
        """

        self.road = road
        if self.road.width < x or x < 0 or y < 0 or y >= self.road.length:
            raise ValueError("Vehicle coordinates out of bound")
        self.x = x              # Vertical position from 0 to width - 1
        self.y = y              # Horizontal position from 0 to length - 1
        self.id = Vehicle.id    # id of vehicle
        Vehicle.id += 1

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

    def get_gap(self, leader: Vehicle) -> int:
        """
        Calculates the gap between two vehicles assuming the given vehicle is ahead and return the absolute value of it.

        :param leader: Other vehicle
        :return: gap - The value of the gap between the vehicle 1 and the vehicle 2
        :author: Mipam Quici
        """
        # Only 1D for now

        gap = leader.y - self.y - leader.length   # Gap is bumper to bumper so [self, 0, 0, leader] is a gap of 2 cells
        if gap < 0:
            gap += self.road.length  # Case in which the leader is at the opposite side of the array but still
            # ahead (infinite road)

        if gap == 0:
            raise ValueError("The gap between Vehicles can't be equal to 0")

        return gap

    def change_lane(self, dest_lane):
        """
        NOT IMPLEMENTED - Changes the lane of the vehicle to the dest_lane.

        :param dest_lane: Lane that the driver wants to reach
        :return: Nothing
        :author: None yet
        """
        pass

    def __str__(self) -> str:
        """
        Overrides __str__ methods for objects

        :return: Id of the vehicle repeated *length* times as a string
        :author: Clément Vellu
        """
        return str(self.id) * self.length

    @abstractmethod
    def draw_image(self, painter: QtGui.QPainter, d_theta: float, radius: int, center: QtCore.QPoint, z: float):
        """
        Abstract method, cannot be called.

        :param painter: Container painter
        :param d_theta: Increment in angle for a gap of one unit in the road array
        :param radius: Radius of the circular road
        :param center: Point that represents the center of the circular road
        :param z: Zooming factor scaling according to the road length
        :return: Nothing
        :author: Clément Vellu
        """
        pass

    @abstractmethod
    def draw_rect(self, painter: QtGui.QPainter, d_theta: float, radius: int, center: QtCore.QPoint, z: float):
        """
        Abstract method, cannot be called.

        :param painter: Container painter
        :param d_theta: Increment in angle for a gap of one unit in the road array
        :param radius: Radius of the circular road
        :param center: Point that represents the center of the circular road
        :param z: Zooming factor scaling according to the road length
        :return: Nothing
        :author: Clément Vellu
        """
        pass


class Car(Vehicle):

    def __init__(self, x, y, road, length=1):
        """
        Initiates the Car class on the given road at given coordinates.

        :param x: Vertical position of the vehicle
        :param y: Horizontal position of the vehicle
        :param road: Road object where the vehicle is located
        :param length: Length of the vehicle
        :author: Clément Vellu
        """
        super().__init__(x, y, road, length)

        self.length = length  # Length of the vehicle, default is 1 slot in the array
        self.speed = 5  # Default speed
        self.ref_speed = 130/3.6  # Desired speed (130 km/h on highways / 36.1 m/s)
        self.smoothness = 4.  # See https://towardsdatascience.com/simulating-traffic-flow-in-python-ee1eab4dd20f
        # for delta explanation and https://traffic-simulation.de/info/info_IDM.html for value
        self.ref_accel = 0.3  # In m²/s
        self.ref_decel = 3.0  # In m²/s
        self.min_gap = 4.  # In meter
        self.react_time = 2.0  # In seconds
        self.type = 1
        if randint(0, 1):
            self.img = QtGui.QImage("imgs/car1.png")
        else:
            self.img = QtGui.QImage("imgs/car2.png")

    def draw_image(self, painter: QtGui.QPainter, d_theta: float, radius: int, center: QtCore.QPoint, z: float):
        """
        Draws the image linked to the Car object on the road at its location.

        :param painter: Container painter
        :param d_theta: Increment in angle for a gap of one unit in the road array
        :param radius: Radius of the circular road
        :param center: Point that represents the center of the circular road
        :param z: Zooming factor scaling according to the road length
        :return: Nothing
        :author: Clément Vellu
        """
        z *= 1.5 # Zooming when using images
        x_circle = radius * np.cos(d_theta * self.y)
        y_circle = - radius * np.sin(d_theta * self.y)
        rect_center = QtCore.QPoint(center.x() + x_circle, center.y() + y_circle)
        veh_rect = QtCore.QRect(- self.length / 2 * z, - self.length / 2 * z, self.length * 2 * z, self.length * z)
        rot_angle_deg = (np.pi / 2 - d_theta * self.y) * 360 / (2 * np.pi)

        painter.save()
        painter.translate(rect_center)
        painter.rotate(rot_angle_deg)
        painter.drawImage(veh_rect, self.img)
        painter.restore()

    def draw_rect(self, painter: QtGui.QPainter, d_theta: float, radius: int, center: QtCore.QPoint, z: float):
        """
        Draws a rectangle at the position of the Car object on the road. The faster the Car goes, the greener the rectangle is.

        :param painter: Container painter
        :param d_theta: Increment in angle for a gap of one unit in the road array
        :param radius: Radius of the circular road
        :param center: Point that represents the center of the circular road
        :param z: Zooming factor scaling according to the road length
        :return: Nothing
        :author: Clément Vellu
        """
        x_circle = radius * np.cos(d_theta * self.y)
        y_circle = - radius * np.sin(d_theta * self.y)
        rect_center = QtCore.QPoint(center.x() + x_circle, center.y() + y_circle)
        veh_rect = QtCore.QRect(- self.length / 2 * z, - self.length / 2 * z, self.length * 2 * z, self.length * z)
        rot_angle_deg = (np.pi / 2 - d_theta * self.y) * 360 / (2 * np.pi)

        painter.save()
        painter.translate(rect_center)
        painter.rotate(rot_angle_deg)
        painter.fillRect(veh_rect, QtGui.QColor(int(255 * (1 - self.speed / self.ref_speed)),
                                                int(255 * (self.speed / self.ref_speed)), 0))
        painter.restore()


class Truck(Vehicle):
    img = QtGui.QImage("imgs/truck1.png")

    def __init__(self, x, y, road, length=3):
        """
        Initiates the Truck class on the given road at given coordinates.

        :param x: Vertical position of the vehicle
        :param y: Horizontal position of the vehicle
        :param road: Road object where the vehicle is located
        :param length: Length of the vehicle
        :author: Clément Vellu
        """
        super().__init__(x, y, road, length)

        self.length = length  # Length of the vehicle, default is 1 slot in the array
        self.speed = 5  # Default speed
        self.ref_speed = 80/3.6  # Desired speed (80 km/h on highways)
        self.smoothness = 4.  # See https://towardsdatascience.com/simulating-traffic-flow-in-python-ee1eab4dd20f
        # for delta explanation and https://traffic-simulation.de/info/info_IDM.html for value
        self.ref_accel = 0.3  # In m²/s
        self.ref_decel = 2.0  # In m²/s
        self.min_gap = 6.  # In meter
        self.react_time = 2.0  # In seconds
        self.type = 2

    def draw_image(self, painter: QtGui.QPainter, d_theta: float, radius: int, center: QtCore.QPoint, z: float):
        """
        Draws the image linked to the Car object on the road at its location.

        :param painter: Container painter
        :param d_theta: Increment in angle for a gap of one unit in the road array
        :param radius: Radius of the circular road
        :param center: Point that represents the center of the circular road
        :param z: Zooming factor scaling according to the road length
        :return: Nothing
        :author: Clément Vellu
        """
        x_circle = radius * np.cos(d_theta * self.y)
        y_circle = - radius * np.sin(d_theta * self.y)
        rect_center = QtCore.QPoint(center.x() + x_circle, center.y() + y_circle)
        veh_rect = QtCore.QRect(- self.length / 2 * z, - self.length / 2 * z, self.length * 2 * z, self.length * z)
        rot_angle_deg = (np.pi / 2 - d_theta * self.y) * 360 / (2 * np.pi)

        painter.save()
        painter.translate(rect_center)
        painter.rotate(rot_angle_deg)
        painter.drawImage(veh_rect, self.img)
        painter.restore()

    def draw_rect(self, painter: QtGui.QPainter, d_theta: float, radius: int, center: QtCore.QPoint, z: float):
        """
        Draws a rectangle at the position of the Truck object on the road. The faster the Car goes, the greener the rectangle is.

        :param painter: Container painter
        :param d_theta: Increment in angle for a gap of one unit in the road array
        :param radius: Radius of the circular road
        :param center: Point that represents the center of the circular road
        :param z: Zooming factor scaling according to the road length
        :return: Nothing
        :author: Clément Vellu
        """
        x_circle = radius * np.cos(d_theta * self.y)
        y_circle = - radius * np.sin(d_theta * self.y)
        rect_center = QtCore.QPoint(center.x() + x_circle, center.y() + y_circle)
        veh_rect = QtCore.QRect(- self.length / 2 * z, - self.length / 2 * z, self.length * 2 * z, self.length * z)
        rot_angle_deg = (np.pi / 2 - d_theta * self.y) * 360 / (2 * np.pi)

        painter.save()
        painter.translate(rect_center)
        painter.rotate(rot_angle_deg)
        painter.fillRect(veh_rect, QtGui.QColor(int(255 * (1 - self.speed / self.ref_speed)),
                                                int(255 * (self.speed / self.ref_speed)), 0))
        painter.restore()

