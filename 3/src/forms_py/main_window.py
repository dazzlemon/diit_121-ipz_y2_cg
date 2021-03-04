# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/forms_ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gview = QtWidgets.QGraphicsView(self.centralwidget)
        self.gview.setObjectName("gview")
        self.gridLayout.addWidget(self.gview, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xDial = QtWidgets.QDial(self.centralwidget)
        self.xDial.setMaximum(360)
        self.xDial.setWrapping(True)
        self.xDial.setObjectName("xDial")
        self.horizontalLayout.addWidget(self.xDial)
        self.yDial = QtWidgets.QDial(self.centralwidget)
        self.yDial.setMaximum(360)
        self.yDial.setWrapping(True)
        self.yDial.setObjectName("yDial")
        self.horizontalLayout.addWidget(self.yDial)
        self.zDial = QtWidgets.QDial(self.centralwidget)
        self.zDial.setMaximum(360)
        self.zDial.setWrapping(True)
        self.zDial.setObjectName("zDial")
        self.horizontalLayout.addWidget(self.zDial)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scaleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.scaleSpinBox.setMinimum(0.1)
        self.scaleSpinBox.setMaximum(10.0)
        self.scaleSpinBox.setSingleStep(0.1)
        self.scaleSpinBox.setProperty("value", 1.0)
        self.scaleSpinBox.setObjectName("scaleSpinBox")
        self.horizontalLayout_3.addWidget(self.scaleSpinBox)
        self.xSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.xSpinBox.setMinimum(-1024)
        self.xSpinBox.setMaximum(1024)
        self.xSpinBox.setObjectName("xSpinBox")
        self.horizontalLayout_3.addWidget(self.xSpinBox)
        self.ySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ySpinBox.setMinimum(-1024)
        self.ySpinBox.setMaximum(1024)
        self.ySpinBox.setObjectName("ySpinBox")
        self.horizontalLayout_3.addWidget(self.ySpinBox)
        self.zSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.zSpinBox.setMinimum(-1024)
        self.zSpinBox.setMaximum(1024)
        self.zSpinBox.setObjectName("zSpinBox")
        self.horizontalLayout_3.addWidget(self.zSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.isoRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.isoRadio.setObjectName("isoRadio")
        self.horizontalLayout_5.addWidget(self.isoRadio)
        self.dimRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.dimRadio.setObjectName("dimRadio")
        self.horizontalLayout_5.addWidget(self.dimRadio)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Safonov Cg3"))
        self.label_3.setText(_translate("MainWindow", "x"))
        self.label.setText(_translate("MainWindow", "y"))
        self.label_2.setText(_translate("MainWindow", "z"))
        self.label_7.setText(_translate("MainWindow", "scale"))
        self.label_6.setText(_translate("MainWindow", "dx"))
        self.label_4.setText(_translate("MainWindow", "dy"))
        self.label_5.setText(_translate("MainWindow", "dz"))
        self.isoRadio.setText(_translate("MainWindow", "isometry"))
        self.dimRadio.setText(_translate("MainWindow", "iso/nen dimetry"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
