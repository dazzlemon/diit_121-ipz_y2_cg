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
        self._plotter = Plotter(QtGui.QColor(0, 255, 0), QtGui.QColor(0, 0, 255), 4)
                     

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
        def close(event): self._widget and self._widget.close()
        def clear_clicked(): 
            self._plotter.clear()
            self._plotter.plot(self._scene)

        self._mainUi.settingsButton.clicked.connect(settings_clicked)
        self._mainUi.plotButton.clicked.connect(plot_clicked)
        self._mainUi.clearButton.clicked.connect(clear_clicked)
        self._mainUi.canvas.resizeEvent = canvas_resized
        self._mainWindow.closeEvent = close


    def _open_plot(self):
        styleVariants = [
            "Normal",
            "Dotted"
        ]
        self._open_widget(Ui_PlotWindow())
        if isinstance(self._uiWidget, Ui_PlotWindow):
            self._uiWidget.funcStyleComboBox.addItems(styleVariants)

            def plot_clicked():
                self._plotter.add_func(PlottableFunction(QtGui.QColor(0, 0, 0), 4, (-3, 3), lambda x: abs(x) + 2 * cos(-x)))# tmp
                self._plotter.add_func(PlottableFunction(QtGui.QColor(255, 0, 255), 4, (0, 6), lambda x: abs(x) - cos(2 * x), PlottableFunction.Style.DOTTED))# tmp
                self._plotter.plot(self._scene)

            self._uiWidget.plotButton.clicked.connect(plot_clicked)

    def _open_settings(self):
        markVariants = [
            "Square",
            "Triangle",
            "Circle"
        ]
        self._open_widget(Ui_SettingsWindow())
        if isinstance(self._uiWidget, Ui_SettingsWindow):
            self._uiWidget.marksStyleComboBox.addItems(markVariants)
            
            def axes_color_clicked():
                colorDialog = QtWidgets.QColorDialog()
                newColor = colorDialog.getColor(self._plotter.axesColor)
                if newColor.isValid():
                    self._plotter.axesColor = newColor
                    self._plotter.plot(self._scene)
            
            def bg_color_clicked():
                colorDialog = QtWidgets.QColorDialog()
                newColor = colorDialog.getColor(self._plotter.bgColor)
                if newColor.isValid():
                    self._plotter.bgColor = newColor
                    self._plotter.plot(self._scene)
                
            self._uiWidget.axesColorButton.clicked.connect(axes_color_clicked)
            self._uiWidget.bgColorButton.clicked.connect(bg_color_clicked)


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
