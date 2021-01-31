from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from forms_py import Ui_MainWindow
from plotter import *
from dialogs import *

class Cg1(QApplication):
    def __init__(self, argv):
        QApplication.__init__(self, argv)

        self._init_main_window() 
        self._widget = None
        self._plotter = Plotter(
            bgColor = QColor(0, 255, 0),
            axesColor = QColor(0, 0, 255),
            axesWidth = 4,
            marksColor = QColor(255, 0, 0),
            marksSize = 10,
            marksStyle = Plotter.MarksStyle.CIRCLE
        )
        
        self._funcs = []
         

    def _init_main_window(self):
        self._mainWindow = QMainWindow()
        self._mainUi = Ui_MainWindow()
        self._mainUi.setupUi(self._mainWindow)

        self._init_canvas()
        self._init_main_window_events() 


    def _init_main_window_events(self):
        def canvas_resized(event):
            self._resize_scene()
            self.plot()

        def settings_clicked(): self._open_settings()
        def plot_clicked(): self._open_plot()
        def close(event): self._widget and self._widget.close()
        def clear_clicked(): 
            self._funcs.clear()
            self.plot()

        self._mainUi.settingsButton.clicked.connect(settings_clicked)
        self._mainUi.plotButton.clicked.connect(plot_clicked)
        self._mainUi.clearButton.clicked.connect(clear_clicked)
        self._mainUi.canvas.resizeEvent = canvas_resized
        self._mainWindow.closeEvent = close


    def _open_plot(self):
        self._open_widget(FunctionPickerDialog)


    def _open_settings(self):
        self._open_widget(PlotterPickerDialog)


    def _init_canvas(self):
        self._scene = QGraphicsScene()
        self._mainUi.canvas.setScene(self._scene)
        self._mainUi.canvas.setAlignment(Qt.AlignTop | Qt.AlignLeft)


    def _open_widget(self, clsWidget):
        if self._widget == None:
            def widget_closed(event): self._widget = None
            self._widget = clsWidget(widget_closed, self)
            self._widget.show()


    def _resize_scene(self):
        x = self._mainUi.canvas.width()
        y = self._mainUi.canvas.height()
        self._scene.setSceneRect(0, 0, x, y)
        self._mainUi.canvas.fitInView(self._scene.sceneRect(), Qt.IgnoreAspectRatio)#still leaves some gaps on sides, seems like a bug

    
    def plot(self):
        self._plotter.plot(self._scene, self._funcs)


    def exec_(self):
        self._mainWindow.show()
        QApplication.exec_()


if __name__ == "__main__":
    import sys
    app = Cg1(sys.argv)
    sys.exit(app.exec_())
