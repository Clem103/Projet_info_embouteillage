# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mipam\Documents\cours\projet python\Projet_info_embouteillage-master\ihm.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_ihm(object):
    def setupUi(self, main_ihm):
        main_ihm.setObjectName("main_ihm")
        main_ihm.resize(802, 586)
        self.centralwidget = QtWidgets.QWidget(main_ihm)
        self.centralwidget.setObjectName("centralwidget")
        self.container = QtWidgets.QWidget(self.centralwidget)
        self.container.setGeometry(QtCore.QRect(20, 10, 771, 301))
        self.container.setObjectName("container")
        self.bouton_simu = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_simu.setGeometry(QtCore.QRect(555, 360, 71, 31))
        self.bouton_simu.setObjectName("bouton_simu")
        self.bouton_pause = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_pause.setGeometry(QtCore.QRect(635, 360, 71, 31))
        self.bouton_pause.setObjectName("bouton_pause")
        self.bouton_quitter = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_quitter.setGeometry(QtCore.QRect(715, 360, 71, 31))
        self.bouton_quitter.setObjectName("bouton_quitter")
        self.slider_vitesse = QtWidgets.QSlider(self.centralwidget)
        self.slider_vitesse.setGeometry(QtCore.QRect(30, 360, 160, 16))
        self.slider_vitesse.setMaximum(100)
        self.slider_vitesse.setOrientation(QtCore.Qt.Horizontal)
        self.slider_vitesse.setObjectName("slider_vitesse")
        self.label_slider_vitesse = QtWidgets.QLabel(self.centralwidget)
        self.label_slider_vitesse.setGeometry(QtCore.QRect(30, 330, 61, 21))
        self.label_slider_vitesse.setObjectName("label_slider_vitesse")
        self.bouton_gen = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_gen.setGeometry(QtCore.QRect(475, 360, 71, 31))
        self.bouton_gen.setObjectName("bouton_gen")
        self.LCD_vitesse = QtWidgets.QLCDNumber(self.centralwidget)
        self.LCD_vitesse.setGeometry(QtCore.QRect(120, 330, 64, 23))
        self.LCD_vitesse.setObjectName("LCD_vitesse")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 330, 201, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_nb_voies = QtWidgets.QLabel(self.layoutWidget)
        self.label_nb_voies.setObjectName("label_nb_voies")
        self.gridLayout.addWidget(self.label_nb_voies, 0, 0, 1, 1)
        self.spinbox_nb_voies = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinbox_nb_voies.setMaximumSize(QtCore.QSize(71, 16777215))
        self.spinbox_nb_voies.setMinimum(1)
        self.spinbox_nb_voies.setMaximum(100000)
        self.spinbox_nb_voies.setObjectName("spinbox_nb_voies")
        self.gridLayout.addWidget(self.spinbox_nb_voies, 0, 1, 1, 1)
        self.label_nb_vehicle = QtWidgets.QLabel(self.layoutWidget)
        self.label_nb_vehicle.setObjectName("label_nb_vehicle")
        self.gridLayout.addWidget(self.label_nb_vehicle, 1, 0, 1, 1)
        self.spinbox_nb_vehicle = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinbox_nb_vehicle.setMaximumSize(QtCore.QSize(71, 16777215))
        self.spinbox_nb_vehicle.setMinimum(1)
        self.spinbox_nb_vehicle.setMaximum(100000)
        self.spinbox_nb_vehicle.setObjectName("spinbox_nb_vehicle")
        self.gridLayout.addWidget(self.spinbox_nb_vehicle, 1, 1, 1, 1)
        self.label_longueur_route = QtWidgets.QLabel(self.layoutWidget)
        self.label_longueur_route.setObjectName("label_longueur_route")
        self.gridLayout.addWidget(self.label_longueur_route, 2, 0, 1, 1)
        self.spinbox_longueur_route = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinbox_longueur_route.setMaximumSize(QtCore.QSize(71, 16777215))
        self.spinbox_longueur_route.setMinimum(100)
        self.spinbox_longueur_route.setMaximum(1000000)
        self.spinbox_longueur_route.setObjectName("spinbox_longueur_route")
        self.gridLayout.addWidget(self.spinbox_longueur_route, 2, 1, 1, 1)
        main_ihm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_ihm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 18))
        self.menubar.setObjectName("menubar")
        main_ihm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_ihm)
        self.statusbar.setObjectName("statusbar")
        main_ihm.setStatusBar(self.statusbar)

        self.retranslateUi(main_ihm)
        self.bouton_quitter.clicked.connect(main_ihm.close)
        self.slider_vitesse.valueChanged['int'].connect(self.LCD_vitesse.display)
        QtCore.QMetaObject.connectSlotsByName(main_ihm)

    def retranslateUi(self, main_ihm):
        _translate = QtCore.QCoreApplication.translate
        main_ihm.setWindowTitle(_translate("main_ihm", "MainWindow"))
        self.bouton_simu.setText(_translate("main_ihm", "Simuler"))
        self.bouton_pause.setText(_translate("main_ihm", "Pause"))
        self.bouton_quitter.setText(_translate("main_ihm", "Quitter"))
        self.label_slider_vitesse.setText(_translate("main_ihm", "Vitesse"))
        self.bouton_gen.setText(_translate("main_ihm", "Générer "))
        self.label_nb_voies.setText(_translate("main_ihm", "Nb de voies "))
        self.label_nb_vehicle.setText(_translate("main_ihm", "Nb véhicules "))
        self.label_longueur_route.setText(_translate("main_ihm", "Longueur route "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_ihm = QtWidgets.QMainWindow()
    ui = Ui_main_ihm()
    ui.setupUi(main_ihm)
    main_ihm.show()
    sys.exit(app.exec_())