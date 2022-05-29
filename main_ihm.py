import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
import ihm
import road
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
        self.ui.spinbox_nb_voies.valueChanged.connect(self.set_road_width)
        self.ui.spinbox_nb_vehicle.valueChanged.connect(self.set_nb_vehicle)
        self.ui.spinbox_longueur_route.valueChanged.connect(self.set_road_length)

        # Setting up background

        roadmap = QtGui.QPixmap("route1.jpg")
        pal = QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(roadmap))
        self.ui.container.lower()
        self.ui.container.stackUnder(self)
        self.ui.container.setAutoFillBackground(True)
        self.ui.container.setPalette(pal)

        # Setting up painter and function called upon container update
        self.painter = QtGui.QPainter()
        self.ui.container.paintEvent = self.drawRoad

        # Setting up simulation with default parameters
        self.road_length = 100
        self.road_width = 1
        self.nb_vehicle = 20
        self.road = None
        self.sim_speed = 1
        self.generer()

    def simuler(self):
        print("Starting / Resetting the simulation")
        if self.timer.isActive():
            self.timer.stop()
        self.timer.start(round(500/self.sim_speed))   # 0.5 is the default time step (simulation running at 100%)

    def one_step(self):
        # Time increment for simulation is always 0.5
        # Otherwise, the physical model doesn't work properly
        step(self.road, time_increment=0.5)
        self.ui.container.update()
        print(self.road)

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

    def set_road_width(self):
        self.road_width = self.ui.spinbox_nb_voies.value()
        print("Changed road width value")

    def set_road_length(self):
        self.road_length = self.ui.spinbox_longueur_route.value()
        print("Changed road length value")

    def generer(self):
        print("Setting up simulation")
        self.road = road.Road(self.road_length, self.road_width, self.nb_vehicle)
        self.ui.container.update()

    def drawRoad(self, *args):  # This function needs to have *args as arguments
        self.painter.begin(self.ui.container)

        for veh in self.road.vehicles:
            self.painter.setPen(QtCore.Qt.green)
            self.painter.drawRect(veh.y * 10, 150, 10 * veh.length, 10)  # Dimensions of the rect are to be changed but it works
        # print("DESSINS DES VOITURES 2ème edition")
        # self.painter.setPen(QtCore.Qt.green)
        # print("DESSIN DES VOITURES 3ème edition")
        # self.painter.drawRect(380,150,50,50)      # au milieu juste pour essayer l'affichage
        # print("DESSIN DES VOITURES END")

        self.painter.end()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
