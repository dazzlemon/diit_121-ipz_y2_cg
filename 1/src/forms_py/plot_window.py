# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms_ui/plot_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlotWindow(object):
    def setupUi(self, PlotWindow):
        PlotWindow.setObjectName("PlotWindow")
        PlotWindow.resize(493, 489)
        self.gridLayout = QtWidgets.QGridLayout(PlotWindow)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.colorButton = QtWidgets.QPushButton(PlotWindow)
        self.colorButton.setObjectName("colorButton")
        self.horizontalLayout_3.addWidget(self.colorButton)
        self.colorView = QtWidgets.QGraphicsView(PlotWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorView.sizePolicy().hasHeightForWidth())
        self.colorView.setSizePolicy(sizePolicy)
        self.colorView.setMinimumSize(QtCore.QSize(20, 20))
        self.colorView.setMaximumSize(QtCore.QSize(20, 20))
        self.colorView.setObjectName("colorView")
        self.horizontalLayout_3.addWidget(self.colorView)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(PlotWindow)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.xMinDoubleSpinBox = QtWidgets.QDoubleSpinBox(PlotWindow)
        self.xMinDoubleSpinBox.setMinimum(-1024.0)
        self.xMinDoubleSpinBox.setMaximum(1024.0)
        self.xMinDoubleSpinBox.setObjectName("xMinDoubleSpinBox")
        self.horizontalLayout.addWidget(self.xMinDoubleSpinBox)
        self.label = QtWidgets.QLabel(PlotWindow)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.xMaxDoubleSpinBox = QtWidgets.QDoubleSpinBox(PlotWindow)
        self.xMaxDoubleSpinBox.setMinimum(-1024.0)
        self.xMaxDoubleSpinBox.setMaximum(1024.0)
        self.xMaxDoubleSpinBox.setObjectName("xMaxDoubleSpinBox")
        self.horizontalLayout.addWidget(self.xMaxDoubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(PlotWindow)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.aDoubleSpinBox = QtWidgets.QDoubleSpinBox(PlotWindow)
        self.aDoubleSpinBox.setMinimum(-1024.0)
        self.aDoubleSpinBox.setMaximum(1024.0)
        self.aDoubleSpinBox.setObjectName("aDoubleSpinBox")
        self.horizontalLayout_2.addWidget(self.aDoubleSpinBox)
        self.label_4 = QtWidgets.QLabel(PlotWindow)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.bDoubleSpinBox = QtWidgets.QDoubleSpinBox(PlotWindow)
        self.bDoubleSpinBox.setMinimum(-1024.0)
        self.bDoubleSpinBox.setMaximum(1024.0)
        self.bDoubleSpinBox.setObjectName("bDoubleSpinBox")
        self.horizontalLayout_2.addWidget(self.bDoubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.plotButton = QtWidgets.QPushButton(PlotWindow)
        self.plotButton.setObjectName("plotButton")
        self.verticalLayout.addWidget(self.plotButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(PlotWindow)
        QtCore.QMetaObject.connectSlotsByName(PlotWindow)

    def retranslateUi(self, PlotWindow):
        _translate = QtCore.QCoreApplication.translate
        PlotWindow.setWindowTitle(_translate("PlotWindow", "Plot new function"))
        self.colorButton.setText(_translate("PlotWindow", "Color"))
        self.label_2.setText(_translate("PlotWindow", "x1"))
        self.label.setText(_translate("PlotWindow", "x2"))
        self.label_3.setText(_translate("PlotWindow", "a"))
        self.label_4.setText(_translate("PlotWindow", "b"))
        self.plotButton.setText(_translate("PlotWindow", "Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotWindow = QtWidgets.QWidget()
    ui = Ui_PlotWindow()
    ui.setupUi(PlotWindow)
    PlotWindow.show()
    sys.exit(app.exec_())
