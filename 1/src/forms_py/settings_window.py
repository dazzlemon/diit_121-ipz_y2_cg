# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms_ui/settings_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(325, 448)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWindow.sizePolicy().hasHeightForWidth())
        SettingsWindow.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(SettingsWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.axesColorButton = QtWidgets.QPushButton(SettingsWindow)
        self.axesColorButton.setObjectName("axesColorButton")
        self.verticalLayout.addWidget(self.axesColorButton)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(SettingsWindow)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.axesWidthSpinBox = QtWidgets.QSpinBox(SettingsWindow)
        self.axesWidthSpinBox.setMinimum(1)
        self.axesWidthSpinBox.setMaximum(64)
        self.axesWidthSpinBox.setObjectName("axesWidthSpinBox")
        self.horizontalLayout_3.addWidget(self.axesWidthSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(SettingsWindow)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.marksStyleComboBox = QtWidgets.QComboBox(SettingsWindow)
        self.marksStyleComboBox.setObjectName("marksStyleComboBox")
        self.horizontalLayout_2.addWidget(self.marksStyleComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(SettingsWindow)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.marksSizeSpinBox = QtWidgets.QSpinBox(SettingsWindow)
        self.marksSizeSpinBox.setMinimum(1)
        self.marksSizeSpinBox.setMaximum(64)
        self.marksSizeSpinBox.setObjectName("marksSizeSpinBox")
        self.horizontalLayout_4.addWidget(self.marksSizeSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.markupColorButton = QtWidgets.QPushButton(SettingsWindow)
        self.markupColorButton.setObjectName("markupColorButton")
        self.verticalLayout.addWidget(self.markupColorButton)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(SettingsWindow)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.markupSizeSpinBox = QtWidgets.QSpinBox(SettingsWindow)
        self.markupSizeSpinBox.setMinimum(1)
        self.markupSizeSpinBox.setMaximum(64)
        self.markupSizeSpinBox.setObjectName("markupSizeSpinBox")
        self.horizontalLayout_5.addWidget(self.markupSizeSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.markupCheckBox = QtWidgets.QCheckBox(SettingsWindow)
        self.markupCheckBox.setObjectName("markupCheckBox")
        self.verticalLayout.addWidget(self.markupCheckBox)
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
        self.label_3.setText(_translate("SettingsWindow", "Axes Width"))
        self.bgColorButton.setText(_translate("SettingsWindow", "Background color"))
        self.textColorButton.setText(_translate("SettingsWindow", "Text color"))
        self.label.setText(_translate("SettingsWindow", "Text size"))
        self.marksColorButton.setText(_translate("SettingsWindow", "Marks color"))
        self.label_2.setText(_translate("SettingsWindow", "Marks style"))
        self.label_4.setText(_translate("SettingsWindow", "Marks size"))
        self.markupColorButton.setText(_translate("SettingsWindow", "Markup color"))
        self.label_5.setText(_translate("SettingsWindow", "Markup size"))
        self.markupCheckBox.setText(_translate("SettingsWindow", "Markup"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QWidget()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()
    sys.exit(app.exec_())
