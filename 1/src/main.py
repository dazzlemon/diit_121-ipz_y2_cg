from PyQt5 import QtWidgets, QtCore, QtGui
from forms_py import *
from plotter import *
from math import cos

class Cg1(QtWidgets.QApplication):
    def __init__(self, argv):
        QtWidgets.QApplication.__init__(self, argv)

        self._init_main_window() 
        self._widget = None
        self._uiWidget = None
        self._plotter = Plotter(QtGui.QColor(0, 255, 0))
        self._plotter.add_func(PlottableFunction(QtGui.QColor(0, 0, 0), 4, (-3, 3), lambda x: abs(x) + 2 * cos(-x)))# tmp
             

    def _init_main_window(self):
        self._mainWindow = QtWidgets.QMainWindow()
        self._mainUi = Ui_MainWindow()
        self._mainUi.setupUi(self._mainWindow)

        self._init_canvas()
        self._init_main_window_events() 


    def _init_main_window_events(self):
        def canvas_resized(event):
            self._resize_scene()
            self._plotter.plot(self._scene)

        def settings_clicked(): self._open_settings()
        def plot_clicked(): self._open_plot()
        def clear_clicked(): print("clear pressed")
        def close(event): self._widget and self._widget.close()

        self._mainUi.settingsButton.clicked.connect(settings_clicked)
        self._mainUi.plotButton.clicked.connect(plot_clicked)
        self._mainUi.clearButton.clicked.connect(clear_clicked)
        self._mainUi.canvas.resizeEvent = canvas_resized
        self._mainWindow.closeEvent = close


    def _open_plot(self):
        self._open_widget(Ui_PlotWindow())


    def _open_settings(self):
        markVariants = [
            "Square",
            "Triangle",
            "Circle"
        ]
        self._open_widget(Ui_SettingsWindow())
        if isinstance(self._uiWidget, Ui_SettingsWindow):
            self._uiWidget.marksStyleComboBox.addItems(markVariants)


    def _init_canvas(self):
        self._scene = QtWidgets.QGraphicsScene()
        self._mainUi.canvas.setScene(self._scene)
        self._mainUi.canvas.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)


    def _open_widget(self, uiWidget):
        def widget_closed(event):
            self._widget = None
            self._uiWidget = None

        if self._widget == None:
            self._widget = QtWidgets.QWidget()
            self._uiWidget = uiWidget
            self._uiWidget.setupUi(self._widget)
            self._widget.closeEvent = widget_closed
            self._widget.show() 


    def _resize_scene(self):
        x = self._mainUi.canvas.width()
        y = self._mainUi.canvas.height()
        self._scene.setSceneRect(0, 0, x, y)
        self._mainUi.canvas.fitInView(self._scene.sceneRect(), QtCore.Qt.IgnoreAspectRatio)#still leaves some gaps on sides, seems like a bug


    def exec_(self):
        self._mainWindow.show()
        QtWidgets.QApplication.exec_()


if __name__ == "__main__":
    import sys
    app = Cg1(sys.argv)
    sys.exit(app.exec_())
