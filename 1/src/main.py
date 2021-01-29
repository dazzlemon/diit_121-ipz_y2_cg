from PyQt5 import QtCore, QtGui, QtWidgets
from forms_py import *


class Cg1:
    def __init__(self, args):
        self.main_ = QtWidgets.QApplication(sys.argv)
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainUi = Ui_MainWindow()
        self.mainUi.setupUi(self.mainWindow)

        self.widget = None
        self.uiWidget = None
        
        def open_widget(uiWidget):
            if self.widget == None:
                self.widget = QtWidgets.QWidget()
                self.uiWidget = uiWidget
                self.uiWidget.setupUi(self.widget)
                self.widget.show()
        

        def settings_clicked(mw):
            def sc(): open_widget(Ui_SettingsWindow())
            return sc


        def clear_clicked(): print("clear pressed")


        def plot_clicked(mw):
            def pc(): open_widget(Ui_PlotWindow())
            return pc


        self.mainUi.settingsButton.clicked.connect(settings_clicked(self.mainUi))
        self.mainUi.plotButton.clicked.connect(plot_clicked(self.mainUi))
        self.mainUi.clearButton.clicked.connect(clear_clicked)


    def run(self):
        self.mainWindow.show()
        sys.exit(self.main_.exec_())


if __name__ == "__main__":
    import sys
    app = Cg1(sys.argv)
    app.run()
