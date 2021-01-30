from PyQt5 import QtWidgets, QtCore, QtGui
from forms_py import *
from plotter import Plotter

class Cg1(QtWidgets.QApplication):
    def __init__(self, argv):
        QtWidgets.QApplication.__init__(self, argv)

        self._init_main_window() 
        self.widget = None
        self.uiWidget = None
        self.plotter = Plotter()
             

    def _init_main_window(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainUi = Ui_MainWindow()
        self.mainUi.setupUi(self.mainWindow)

        self._init_canvas()
        self._init_main_window_events() 


    def _init_main_window_events(self):
        def canvas_resized(event):
            self.resize_scene()
            self.plotter.plot(self.scene)

        def settings_clicked(): self._open_settings()
        def plot_clicked(): self._open_plot()
        def clear_clicked(): print("clear pressed")
        def close(event): self.widget and self.widget.close()

        self.mainUi.settingsButton.clicked.connect(settings_clicked)
        self.mainUi.plotButton.clicked.connect(plot_clicked)
        self.mainUi.clearButton.clicked.connect(clear_clicked)
        self.mainUi.canvas.resizeEvent = canvas_resized
        self.mainWindow.closeEvent = close


    def _open_plot(self):
        self.open_widget(Ui_PlotWindow())


    def _open_settings(self):
        markVariants = [
            "Square",
            "Triangle",
            "Circle"
        ]
        self.open_widget(Ui_SettingsWindow())
        if isinstance(self.uiWidget, Ui_SettingsWindow):
            self.uiWidget.marksStyleComboBox.addItems(markVariants)


    def _init_canvas(self):
        self.scene = QtWidgets.QGraphicsScene()
        self.mainUi.canvas.setScene(self.scene)
        self.mainUi.canvas.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)


    def open_widget(self, uiWidget):
        def widget_closed(event):
            self.widget = None
            self.uiWidget = None

        if self.widget == None:
            self.widget = QtWidgets.QWidget()
            self.uiWidget = uiWidget
            self.uiWidget.setupUi(self.widget)
            self.widget.closeEvent = widget_closed
            self.widget.show() 


    def resize_scene(self):
        x = self.mainUi.canvas.width()
        y = self.mainUi.canvas.height()
        self.scene.setSceneRect(0, 0, x, y)
        self.mainUi.canvas.fitInView(self.scene.sceneRect(), QtCore.Qt.IgnoreAspectRatio)#still leaves some gaps on sides, seems like a bug


    def exec_(self):
        self.mainWindow.show()
        QtWidgets.QApplication.exec_()


if __name__ == "__main__":
    import sys
    app = Cg1(sys.argv)
    sys.exit(app.exec_())
