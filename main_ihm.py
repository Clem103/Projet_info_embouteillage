import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
import ihm
import road
import vehicle



class MonAppli(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=ihm.Ui_main_ihm()
        self.ui.setupUi(self)

        self.ui.bouton_simu.clicked.connect(self.simuler)
        self.ui.bouton_quitter.clicked.connect(self.quitter)
        self.ui.bouton_pause.clicked.connect(self.pause)
        #self.ui.slider_vitesse.sliderPressed.connect(self.vitesse)
        self.ui.bouton_gen.clicked.connect(self.generer)
        self.ui.spinbox_nb_voies.valueChanged.connect(self.nb_voies)
        self.ui.spinbox_nb_vehicle.valueChanged.connect(self.nb_vehicle)
        self.ui.spinbox_longueur_route.valueChanged.connect(self.longueur_route)
        self.ui.slider_vitesse.sliderReleased.connect(self.vitesse)

        self.longueur_route()
        self.vitesse()
        self.nb_voies()
        self.nb_vehicle()

        roadmap=QtGui.QPixmap("route1.png")
        pal=QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(roadmap))
        self.ui.container.lower()
        self.ui.container.stackUnder(self)
        self.ui.container.setAutoFillBackground(True)
        self.ui.container.setPalette(pal)

        self.painter=QtGui.QPainter()
        self.ui.container.paintEvent=self.drawRoad()


        self.generer()

    def simuler(self):
        self.ui.container.update()
        print("appel de la fonction simuler")

    def pause(self):
        print("appel de la fonction pause")

    def quitter(self):
        print("appel de la fonction quitter")

    def vitesse(self):
        print("appel du slider vitesse")
        self.vitesse = self.ui.LCD_vitesse.value()
        #print(self.vitesse)

    def nb_vehicle(self):
        self.nb_vehic = self.ui.spinbox_nb_vehicle.value()
        print("appel du spinbox nb de véhicle")
        #print("nb vehic=",self.nb_vehic)

    def nb_voies(self):
        self.nbvoies = self.ui.spinbox_nb_voies.value()
        print("appel du spinbox nb de voies")
        #print("nb voies=",self.nbvoies)


    def longueur_route(self):
        self.long = self.ui.spinbox_longueur_route.value()
        print("appel du spinbox longueur route")
        #print("longueur route=",self.long)


    def generer(self):
        self.ui.container.update()
        print("appel de la fonction générer")
        print(road.Road(self.long,self.nbvoies,self.nb_vehic))
        self.ui.container.update()

    def drawRoad(self):
        print("DESSIN DES VOITURES")
        self.painter.begin(self.ui.container)

#        for i in range(self.nb_vehic):
#            self.painter.setPen(QtCore.Qt.green)
#            self.painter.drawRect(150,road.Road.L(road.Road(self.long,self.nbvoies,self.nb_vehic))[i],50,50)
        print("DESSINS DES VOITURES 2ème edition")
        self.painter.setPen(QtCore.Qt.green)
        print("DESSIN DES VOITURES 3ème edition")
        self.painter.drawRect(380,150,50,50)      # au milieu juste pour essayer l'affichage
        print("DESSIN DES VOITURES END")

        self.painter.end()





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
