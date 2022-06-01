import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
import ihm
import road
import numpy as np
from simulation import step


class MonAppli(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Initiates the UI with a new Road.
        :return: Nothing
        :author: Clément Vellu
        """
        super().__init__()

        # Setting up the UI

        self.ui = ihm.Ui_main_ihm()
        self.ui.setupUi(self)

        # Setting up timer for simulation speed

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.one_step)

        # Connecting the buttons to functions

        self.ui.bouton_simu.clicked.connect(self.simulate)
        self.ui.bouton_pause.clicked.connect(self.pause)
        self.ui.slider_vitesse.valueChanged.connect(self.set_sim_speed)
        self.ui.bouton_gen.clicked.connect(self.generate_sim)
        self.ui.spinbox_nb_vehicle.valueChanged.connect(self.set_nb_vehicle)
        self.ui.spinbox_longueur_route.valueChanged.connect(self.set_road_length)
        self.ui.disp_img.valueChanged.connect(self.switch_display)

        # Setting up background

        fond = QtGui.QPixmap("imgs/fond.jpg").scaled(self.ui.container.width(), self.ui.container.height(), QtCore.Qt.KeepAspectRatio)
        pal = QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(fond))
        self.ui.container.lower()
        self.ui.container.stackUnder(self)
        self.ui.container.setAutoFillBackground(True)
        self.ui.container.setPalette(pal)

        # Setting up painter and function called upon container update
        self.painter = QtGui.QPainter()
        self.ui.container.paintEvent = self.update_screen

        # Setting up simulation with default parameters
        self.road_length = 500
        self.road_width = 1
        self.nb_vehicle = 40
        self.road = None
        self.sim_speed = 1
        self.disp_img = 1

        self.generate_sim()

    def simulate(self):
        """
        Sets the speed of the simulation.

        :return: Nothing
        :author: Clément Vellu
        """
        print("Starting / Resetting the simulation")
        if self.timer.isActive():
            self.timer.stop()
        self.timer.start(round(30/self.sim_speed))   # 0.5 is the default time step (simulation running at 100%)

    def one_step(self):
        """
        Performs a step of the simulation. Uses step function from simulation script. Updates the display

        :return: Nothing
        :author: Clément Vellu
        """
        # Time increment for simulation is always 0.5
        # Otherwise, the physical model doesn't work properly
        step(self.road, time_increment=0.5)
        self.ui.container.update()

    def pause(self):
        """
        Pauses the simulation.

        :return: Nothing
        :author: Clément Vellu
        """
        print("Pausing the simulation")
        self.timer.stop()

    def set_sim_speed(self):
        """
        Called upon simulation speed slider change. Changes the simulation speed.

        :return: Nothing
        :author: Clément Vellu
        """
        print("Changed simulation speed")
        self.sim_speed = self.ui.LCD_vitesse.value() / 100
        if self.timer.isActive():
            self.simulate()

    def set_nb_vehicle(self):
        """
        Sets the number of Vehicles on the Road.

        :return: Nothing
        :author: Clément Vellu
        """
        self.nb_vehicle = self.ui.spinbox_nb_vehicle.value()
        self.generate_sim()
        print("Changed number of vehicles")

    def set_road_length(self):
        """
        Sets the road length.

        :return: Nothing
        :author: Clément Vellu
        """
        self.road_length = self.ui.spinbox_longueur_route.value()
        self.generate_sim()
        print("Changed road length value")

    def generate_sim(self):
        """
        Generates a Road and updates the display.

        :return: Nothing
        :author: Clément Vellu
        """
        print("Setting up simulation")
        self.road = road.Road(self.road_length, self.road_width, self.nb_vehicle)
        self.ui.container.update()

    def update_screen(self, *args):
        """
        Updates the container display and the LCDs.

        :return: Nothing
        :author: Clément Vellu
        """

        # Update mean speed LCD display

        self.ui.LCD_vitesse_moy.display('{:.02f}'.format(self.road.get_mean_speed(0, 0) * 3.6))

        # Init container painter
        self.painter.begin(self.ui.container)

        # Draw road
        width = self.ui.container.width()
        height = self.ui.container.height()
        radius = min(int(height * 0.45), int(width * 0.45))
        center = QtCore.QPoint(width // 2, height // 2)

        self.draw_road(width, height, radius, center)

        # Draw vehicles
        z = 2000 / self.road_length  # Zooming factor
        for veh in self.road.vehicles:

            d_theta = 2*np.pi/self.road_length

            if not self.disp_img:
                veh.draw_rect(self.painter, d_theta, radius, center, z)
            else:
                veh.draw_image(self.painter, d_theta, radius, center, z)

        self.painter.end()

    def draw_road(self, width: int, height: int, radius: int, center: QtCore.QPoint):
        """
        Draws the road on the display.

        :param width: Width of the container
        :param height: Height of the container
        :param radius: Radius of the road
        :param center: Center of the circular road
        :return: Nothing
        :author: Clément Vellu
        """

        pen = QtGui.QPen()
        pen.setStyle(QtCore.Qt.SolidLine)
        pen.setWidth(60)
        pen.setBrush(QtCore.Qt.black)
        self.painter.setPen(pen)
        self.painter.drawEllipse(center, radius, radius)
        pen.setStyle(QtCore.Qt.SolidLine)
        pen.setWidth(5)
        pen.setBrush(QtCore.Qt.white)
        self.painter.setPen(pen)
        self.painter.drawEllipse(center, min(int(height * 0.42), int(width * 0.42)),
                                 min(int(height * 0.42), int(width * 0.42)))
        self.painter.drawEllipse(center, min(int(height * 0.48), int(width * 0.48)),
                                 min(int(height * 0.48), int(width * 0.48)))

    def switch_display(self):
        """
        Called upon switch on the display mode slider. Updates the type of display for the Vehicles

        :return: Nothing
        :author: Clément Vellu
        """
        self.disp_img = self.ui.disp_img.value()
        self.ui.container.update()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
