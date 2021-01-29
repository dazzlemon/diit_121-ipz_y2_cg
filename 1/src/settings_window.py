# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(379, 417)
        self.gridLayout = QtWidgets.QGridLayout(SettingsWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.axesColorButton = QtWidgets.QPushButton(SettingsWindow)
        self.axesColorButton.setObjectName("axesColorButton")
        self.verticalLayout.addWidget(self.axesColorButton)
        self.bgColorButton = QtWidgets.QPushButton(SettingsWindow)
        self.bgColorButton.setObjectName("bgColorButton")
        self.verticalLayout.addWidget(self.bgColorButton)
        self.textColorButton = QtWidgets.QPushButton(SettingsWindow)
        self.textColorButton.setObjectName("textColorButton")
        self.verticalLayout.addWidget(self.textColorButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SettingsWindow)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textSizeSpinBox = QtWidgets.QSpinBox(SettingsWindow)
        self.textSizeSpinBox.setMinimum(1)
        self.textSizeSpinBox.setMaximum(64)
        self.textSizeSpinBox.setObjectName("textSizeSpinBox")
        self.horizontalLayout.addWidget(self.textSizeSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.marksColorButton = QtWidgets.QPushButton(SettingsWindow)
        self.marksColorButton.setObjectName("marksColorButton")
        self.verticalLayout.addWidget(self.marksColorButton)
        self.marksStyleComboBox = QtWidgets.QComboBox(SettingsWindow)
        self.marksStyleComboBox.setObjectName("marksStyleComboBox")
        self.verticalLayout.addWidget(self.marksStyleComboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Canvas Settings"))
        self.axesColorButton.setText(_translate("SettingsWindow", "Axes color"))
        self.bgColorButton.setText(_translate("SettingsWindow", "Background color"))
        self.textColorButton.setText(_translate("SettingsWindow", "Text color"))
        self.label.setText(_translate("SettingsWindow", "Text size"))
        self.marksColorButton.setText(_translate("SettingsWindow", "Marks color"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QWidget()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()
    sys.exit(app.exec_())
