import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
import ihm
import road
import numpy as np
from simulation import step


class MonAppli(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting up the UI

        self.ui = ihm.Ui_main_ihm()
        self.ui.setupUi(self)

        # Setting up timer for simulation speed

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.one_step)

        # Connecting the buttons to functions

        self.ui.bouton_simu.clicked.connect(self.simuler)
        self.ui.bouton_pause.clicked.connect(self.pause)
        self.ui.slider_vitesse.valueChanged.connect(self.set_sim_speed)
        self.ui.bouton_gen.clicked.connect(self.generer)
        self.ui.spinbox_nb_vehicle.valueChanged.connect(self.set_nb_vehicle)
        self.ui.spinbox_longueur_route.valueChanged.connect(self.set_road_length)
        self.ui.disp_img.valueChanged.connect(self.switch_display)

        # Setting up background

        fond = QtGui.QPixmap("fond.jpg").scaled(self.ui.container.width(), self.ui.container.height(), QtCore.Qt.KeepAspectRatio)
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

        self.generer()

    def simuler(self):
        print("Starting / Resetting the simulation")
        if self.timer.isActive():
            self.timer.stop()
        self.timer.start(round(30/self.sim_speed))   # 0.5 is the default time step (simulation running at 100%)

    def one_step(self):
        # Time increment for simulation is always 0.5
        # Otherwise, the physical model doesn't work properly
        step(self.road, time_increment=0.5)
        self.ui.container.update()
        # print(self.road) for debugging purpose

    def pause(self):
        print("Pausing the simulation")
        self.timer.stop()

    def set_sim_speed(self):
        print("Changed simulation speed")
        self.sim_speed = self.ui.LCD_vitesse.value() / 100
        if self.timer.isActive():
            self.simuler()

    def set_nb_vehicle(self):
        self.nb_vehicle = self.ui.spinbox_nb_vehicle.value()
        print("Changed number of vehicles")

    def set_road_length(self):
        self.road_length = self.ui.spinbox_longueur_route.value()
        print("Changed road length value")

    def generer(self):
        print("Setting up simulation")
        self.road = road.Road(self.road_length, self.road_width, self.nb_vehicle)
        self.ui.container.update()

    def update_screen(self, *args):  # This function needs to have *args as arguments

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
        for veh in self.road.vehicles:

            d_theta = 2*np.pi/self.road_length
            z = 2000/self.road_length # Zooming factor

            if not self.disp_img:
                veh.draw_rect(self.painter, d_theta, radius, center, z)
            else:
                veh.draw_image(self.painter, d_theta, radius, center, z)

        self.painter.end()

    def draw_road(self, width, height, radius, center):

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
        self.disp_img = self.ui.disp_img.value()
        self.ui.container.update()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
