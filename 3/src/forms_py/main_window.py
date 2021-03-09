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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout_3.addWidget(self.doubleSpinBox_5, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 0, 3, 4, 1)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout_3.addWidget(self.doubleSpinBox_8, 2, 1, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_3.addWidget(self.doubleSpinBox_2, 0, 1, 1, 1)
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.gridLayout_3.addWidget(self.doubleSpinBox_11, 2, 2, 1, 1)
        self.doubleSpinBox_15 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_15.setObjectName("doubleSpinBox_15")
        self.gridLayout_3.addWidget(self.doubleSpinBox_15, 0, 6, 1, 1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout_3.addWidget(self.doubleSpinBox_7, 1, 1, 1, 1)
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.gridLayout_3.addWidget(self.doubleSpinBox_12, 3, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 0, 7, 4, 1)
        self.doubleSpinBox_17 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_17.setObjectName("doubleSpinBox_17")
        self.gridLayout_3.addWidget(self.doubleSpinBox_17, 0, 9, 1, 1)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.gridLayout_3.addWidget(self.doubleSpinBox_9, 3, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(4)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 0, 11, 4, 1)
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.gridLayout_3.addWidget(self.doubleSpinBox_10, 1, 2, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout_3.addWidget(self.doubleSpinBox_6, 3, 0, 1, 1)
        self.doubleSpinBox_13 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_13.setObjectName("doubleSpinBox_13")
        self.gridLayout_3.addWidget(self.doubleSpinBox_13, 0, 4, 1, 1)
        self.doubleSpinBox_19 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_19.setObjectName("doubleSpinBox_19")
        self.gridLayout_3.addWidget(self.doubleSpinBox_19, 0, 12, 1, 1)
        self.doubleSpinBox_14 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_14.setObjectName("doubleSpinBox_14")
        self.gridLayout_3.addWidget(self.doubleSpinBox_14, 0, 5, 1, 1)
        self.doubleSpinBox_18 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_18.setObjectName("doubleSpinBox_18")
        self.gridLayout_3.addWidget(self.doubleSpinBox_18, 0, 10, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_3.addWidget(self.doubleSpinBox_4, 1, 0, 1, 1)
        self.doubleSpinBox_20 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_20.setObjectName("doubleSpinBox_20")
        self.gridLayout_3.addWidget(self.doubleSpinBox_20, 0, 13, 1, 1)
        self.doubleSpinBox_16 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_16.setObjectName("doubleSpinBox_16")
        self.gridLayout_3.addWidget(self.doubleSpinBox_16, 0, 8, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_3.addWidget(self.doubleSpinBox, 0, 0, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_3.addWidget(self.doubleSpinBox_3, 0, 2, 1, 1)
        self.doubleSpinBox_21 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_21.setObjectName("doubleSpinBox_21")
        self.gridLayout_3.addWidget(self.doubleSpinBox_21, 0, 14, 1, 1)
        self.doubleSpinBox_22 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_22.setObjectName("doubleSpinBox_22")
        self.gridLayout_3.addWidget(self.doubleSpinBox_22, 1, 4, 1, 1)
        self.doubleSpinBox_23 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_23.setObjectName("doubleSpinBox_23")
        self.gridLayout_3.addWidget(self.doubleSpinBox_23, 1, 5, 1, 1)
        self.doubleSpinBox_24 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_24.setObjectName("doubleSpinBox_24")
        self.gridLayout_3.addWidget(self.doubleSpinBox_24, 1, 6, 1, 1)
        self.doubleSpinBox_25 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_25.setObjectName("doubleSpinBox_25")
        self.gridLayout_3.addWidget(self.doubleSpinBox_25, 2, 4, 1, 1)
        self.doubleSpinBox_26 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_26.setObjectName("doubleSpinBox_26")
        self.gridLayout_3.addWidget(self.doubleSpinBox_26, 2, 5, 1, 1)
        self.doubleSpinBox_27 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_27.setObjectName("doubleSpinBox_27")
        self.gridLayout_3.addWidget(self.doubleSpinBox_27, 2, 6, 1, 1)
        self.doubleSpinBox_28 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_28.setObjectName("doubleSpinBox_28")
        self.gridLayout_3.addWidget(self.doubleSpinBox_28, 3, 4, 1, 1)
        self.doubleSpinBox_29 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_29.setObjectName("doubleSpinBox_29")
        self.gridLayout_3.addWidget(self.doubleSpinBox_29, 3, 5, 1, 1)
        self.doubleSpinBox_30 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_30.setObjectName("doubleSpinBox_30")
        self.gridLayout_3.addWidget(self.doubleSpinBox_30, 3, 6, 1, 1)
        self.doubleSpinBox_31 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_31.setObjectName("doubleSpinBox_31")
        self.gridLayout_3.addWidget(self.doubleSpinBox_31, 1, 8, 1, 1)
        self.doubleSpinBox_32 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_32.setObjectName("doubleSpinBox_32")
        self.gridLayout_3.addWidget(self.doubleSpinBox_32, 1, 9, 1, 1)
        self.doubleSpinBox_33 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_33.setObjectName("doubleSpinBox_33")
        self.gridLayout_3.addWidget(self.doubleSpinBox_33, 1, 10, 1, 1)
        self.doubleSpinBox_34 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_34.setObjectName("doubleSpinBox_34")
        self.gridLayout_3.addWidget(self.doubleSpinBox_34, 2, 8, 1, 1)
        self.doubleSpinBox_35 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_35.setObjectName("doubleSpinBox_35")
        self.gridLayout_3.addWidget(self.doubleSpinBox_35, 2, 9, 1, 1)
        self.doubleSpinBox_36 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_36.setObjectName("doubleSpinBox_36")
        self.gridLayout_3.addWidget(self.doubleSpinBox_36, 2, 10, 1, 1)
        self.doubleSpinBox_37 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_37.setObjectName("doubleSpinBox_37")
        self.gridLayout_3.addWidget(self.doubleSpinBox_37, 3, 8, 1, 1)
        self.doubleSpinBox_38 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_38.setObjectName("doubleSpinBox_38")
        self.gridLayout_3.addWidget(self.doubleSpinBox_38, 3, 9, 1, 1)
        self.doubleSpinBox_39 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_39.setObjectName("doubleSpinBox_39")
        self.gridLayout_3.addWidget(self.doubleSpinBox_39, 3, 10, 1, 1)
        self.doubleSpinBox_40 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_40.setObjectName("doubleSpinBox_40")
        self.gridLayout_3.addWidget(self.doubleSpinBox_40, 1, 12, 1, 1)
        self.doubleSpinBox_41 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_41.setObjectName("doubleSpinBox_41")
        self.gridLayout_3.addWidget(self.doubleSpinBox_41, 2, 12, 1, 1)
        self.doubleSpinBox_42 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_42.setObjectName("doubleSpinBox_42")
        self.gridLayout_3.addWidget(self.doubleSpinBox_42, 3, 12, 1, 1)
        self.doubleSpinBox_43 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_43.setObjectName("doubleSpinBox_43")
        self.gridLayout_3.addWidget(self.doubleSpinBox_43, 1, 13, 1, 1)
        self.doubleSpinBox_44 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_44.setObjectName("doubleSpinBox_44")
        self.gridLayout_3.addWidget(self.doubleSpinBox_44, 2, 13, 1, 1)
        self.doubleSpinBox_45 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_45.setObjectName("doubleSpinBox_45")
        self.gridLayout_3.addWidget(self.doubleSpinBox_45, 3, 13, 1, 1)
        self.doubleSpinBox_46 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_46.setObjectName("doubleSpinBox_46")
        self.gridLayout_3.addWidget(self.doubleSpinBox_46, 1, 14, 1, 1)
        self.doubleSpinBox_47 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_47.setObjectName("doubleSpinBox_47")
        self.gridLayout_3.addWidget(self.doubleSpinBox_47, 2, 14, 1, 1)
        self.doubleSpinBox_48 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_48.setObjectName("doubleSpinBox_48")
        self.gridLayout_3.addWidget(self.doubleSpinBox_48, 3, 14, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
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
        self.groupBox.setTitle(_translate("MainWindow", "P matrix for Bezier surface"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
